## NOTE STILL A WORK IN PROGRESS...NOT FULLY DEPLOYED ##

# RNA-seq Pipeline Sample Sheet Generator

This Python script automates the creation of sample sheets for RNA-seq, Sarek, and Taxprofiler pipelines, as well as dynamically updates the corresponding `params.json` files for each pipeline. It is designed to streamline the setup for running different NF-core pipelines by preparing all necessary input files and parameters based on user-provided fastq files.

## Features

- **Sample Sheet Creation**: Automatically generates sample sheets specific to RNA-seq, Sarek, and Taxprofiler pipelines.
- **Dynamic Params Update**: Updates the `params.json` files specific to each pipeline, adding paths for the newly created sample sheet and a results directory.
- **Modular Design**: Easily extendable to add more pipelines or handle additional functionalities.
- **Environment-Aware**: Uses environment variables to adapt to different system configurations.

## Requirements

- Python 3.6 or higher
- Unix-like operating system (Linux, MacOS)
- Access to a set of fastq files for processing

## Installation
No additional installation steps are required beyond having Python installed. Clone this repository or download the script directly to your system.

```
git clone https://your-repository-url
cd your-repository-directory
```

## Usage
Run the script from the command line by providing the path to the directory containing the fastq files. The script will prompt for the necessary inputs during execution.

```
python3 nfcore_pipeline_samplesheet.py /path/to/your/fastq_files
```
### Step-by-step Execution

1. **Specify Fastq Directory**: Provide the full path to the directory containing your fastq files.
2. **Select Pipeline**: Choose which pipeline's sample sheet to generate (RNA-seq, Sarek, or Taxprofiler).
3. **For Sarek**: If Sarek is selected, specify the sample processing method (`method1` for concatenated or `method2` for multilane processing).

After these inputs are provided, the script will:
- Create the sample sheet in the specified directory.
- Update the corresponding `params.json` in the pipeline directory under the user's `.nextflow/nf-core/` directory.
- Create a `results` directory within the same directory as the sample sheets for output data storage.

## Output

The script outputs:
- A pipeline-specific sample sheet CSV file.
- An updated `params.json` file with paths set to the newly created sample sheet and results directory.
- A results directory ready to store pipeline output.

## Contributing

Contributions to this script are welcome. Please fork the repository and submit pull requests with any enhancements, bug fixes, or suggestions. For major changes, please open an issue first to discuss what you would like to change.

## License

This script is distributed under the MIT License. See `LICENSE` for more information.

## Contact

For any queries regarding the script, please contact me (Andrew Geller gellerand@gmail.com)
