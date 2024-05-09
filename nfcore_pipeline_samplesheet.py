#!/usr/bin/env python
# Main python script for nfcore_pipeline_samplesheet
print(f'Current working directory is: {os.getcwd()}')
import os
import sys
import logging
from pathlib import Path
import csv

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def find_fastq_pairs(directory):
    """Scan the directory and return a dictionary mapping sample prefix to fastq file pairs."""
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
    # Sort files to ensure R1/R2 order
    for prefix in fastq_files:
        fastq_files[prefix].sort()
    return fastq_files

def write_rnaseq_samplesheet(output_path, fastq_dict):
    """Write the RNA-seq sample sheet."""
    with open(output_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['sample', 'fastq_1', 'fastq_2', 'strandedness'])
        for sample, files in fastq_dict.items():
            if len(files) == 2:
                writer.writerow([sample, files[0], files[1], 'auto'])
            else:
                logging.error(f"Sample {sample} does not have exactly two fastq files.")

def write_sarek_samplesheet(output_path, fastq_dict, method):
    """Write the Sarek sample sheet."""
    with open(output_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['patient', 'sample', 'lane', 'fastq_1', 'fastq_2'])
        for sample, files in fastq_dict.items():
            if method == 'method1':
                if len(files) == 2:
                    writer.writerow([sample, sample, 1, files[0], files[1]])
                else:
                    logging.error(f"Sample {sample} does not have exactly two fastq files for method 1.")
            elif method == 'method2':
                lane_count = 1
                for file_pair in zip(files[::2], files[1::2]):
                    writer.writerow([sample, sample, f'lane_{lane_count}', file_pair[0], file_pair[1]])
                    lane_count += 1

def write_taxprofiler_samplesheet(output_path, fastq_dict):
    """Write the Taxprofiler sample sheet."""
    with open(output_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['sample', 'run_accession', 'instrument_platform', 'fastq_1', 'fastq_2', 'fasta'])
        for sample, files in fastq_dict.items():
            if len(files) == 2:
                writer.writerow([sample, 'run1', 'ILLUMINA', files[0], files[1], ''])
            else:
                logging.error(f"Sample {sample} does not have exactly two fastq files.")

def main():
    directory = input("Please provide path to fastq files: ")
    fastq_dict = find_fastq_pairs(directory)

    if not fastq_dict:
        logging.error("No fastq files found in the directory or directory does not exist.")
        sys.exit(1)

    run_name = Path(directory).parent.name
    pipeline = input("Select pipeline for sample sheet creation (rnaseq, sarek, taxprofiler): ").lower()
    output_path = os.path.join(directory, f'{run_name}_samplesheet.csv')

    if pipeline == 'rnaseq':
        write_rnaseq_samplesheet(output_path, fastq_dict)
    elif pipeline == 'sarek':
        method = input("Concatenated (method1) or Multilane (method2): ").lower()
        write_sarek_samplesheet(output_path, fastq_dict, method)
    elif pipeline == 'taxprofiler':
        write_taxprofiler_samplesheet(output_path, fastq_dict)
    else:
        logging.error("Invalid pipeline selection.")
        sys.exit(1)

    logging.info("Sample sheet creation complete at %s", output_path)

if __name__ == "__main__":
    main()
