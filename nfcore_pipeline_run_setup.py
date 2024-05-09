import os
import sys
import logging
import json
from pathlib import Path
import csv

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def find_fastq_pairs(directory):
    """Scan the directory for fastq file pairs and return a dictionary mapping sample prefix to file pairs."""
    if not Path(directory).exists():
        logging.error(f"The directory {directory} does not exist.")
        return {}
    fastq_files = {}
    for file in Path(directory).rglob('*.fastq.gz'):
        prefix = '_'.join(file.stem.split('_')[:-2])
        if prefix in fastq_files:
            fastq_files[prefix].append(str(file))
        else:
            fastq_files[prefix] = [str(file)]
    for prefix in fastq_files:
        fastq_files[prefix].sort()
    return fastq_files

def write_samplesheet(pipeline, output_path, fastq_dict):
    """Write sample sheets based on the pipeline."""
    if pipeline == 'rnaseq':
        fields = ['sample_name', 'fastq_1', 'fastq_2']
    elif pipeline == 'sarek':
        fields = ['sample_name', 'fastq_1', 'fastq_2', 'method']
    elif pipeline == 'taxprofiler':
        fields = ['sample_name', 'fastq_files']
    
    with open(output_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        for sample, files in fastq_dict.items():
            if len(files) >= 2:
                row = {'sample_name': sample, 'fastq_1': files[0], 'fastq_2': files[1]}
                if pipeline == 'sarek':
                    row['method'] = 'your_method_here'  # Adjust as necessary
                elif pipeline == 'taxprofiler':
                    row = {'sample_name': sample, 'fastq_files': ','.join(files)}
                writer.writerow(row)

def update_params(pipeline, directory, sample_sheet_path):
    """Update the params.json file for the selected pipeline."""
    run_name = Path(directory).parent.stem
    base_params_path = Path.home().joinpath(f".nextflow/nf-core/{pipeline.upper()}/params.json")

    if not base_params_path.exists():
        logging.error(f"Base params.json not found at {base_params_path}")
        return

    results_dir = Path(directory).parent / 'results'
    results_dir.mkdir(parents=True, exist_ok=True)

    try:
        with base_params_path.open('r') as file:
            params = json.load(file)
        params['input'] = str(sample_sheet_path)
        params['outdir'] = str(results_dir)

        new_params_path = results_dir.parent / f'{run_name}_{pipeline}_params.json'
        with new_params_path.open('w') as file:
            json.dump(params, file, indent=4)
        logging.info(f"Updated params.json created at {new_params_path}")
    except json.JSONDecodeError:
        logging.error("Error decoding JSON from the base params.json file.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

def main():
    directory = input("Please provide path to fastq files: ")
    fastq_dict = find_fastq_pairs(directory)
    if not fastq_dict:
        logging.error("No fastq files found or directory does not exist.")
        sys.exit(1)

    run_name = Path(directory).parent.stem
    pipeline = input("Select pipeline (rnaseq, sarek, taxprofiler): ").lower()
    output_path = Path(directory).parent / f'{run_name}_samplesheet.csv'
    write_samplesheet(pipeline, output_path, fastq_dict)
    update_params(pipeline, directory, output_path)
    logging.info("Sample sheet and params.json creation complete.")

if __name__ == "__main__":
    main()