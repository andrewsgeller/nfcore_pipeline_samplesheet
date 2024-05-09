# Fastq Sample Sheet Generator

# Overview
This script automates the creation of sample sheets for different bioinformatics pipelines based on fastq files. It is designed to handle RNA-seq, Sarek, and Taxprofiler pipelines, ensuring the correct format for each. The script allows for input of a directory containing fastq files and generates a corresponding sample sheet in the same directory, named according to the run name extracted from the directory structure.

# Features
Automated Sample Sheet Creation: Automatically creates sample sheets for RNA-seq, Sarek, and Taxprofiler pipelines.
Run Name Extraction: Extracts the run name from the directory just above the fastq files for naming the sample sheet.
Error Handling: Robust error checking for directory existence, file patterns, and ensuring each sample has exactly two fastq files (where applicable).

# Requirements
Python 3.6 or higher
pathlib, which should be included in standard Python installations
Setup and Installation
No additional libraries are required beyond the standard Python installation. Simply download the script to your local machine.

# Usage
To use this script, navigate to the directory where the script is located in your command line interface and run it using Python. You will be prompted to input necessary details:

# Path to Fastq Files: Input the full path to the directory containing your fastq files.
Pipeline Selection: Choose the pipeline for which you want to create a sample sheet (rnaseq, sarek, taxprofiler).
Method (Only for Sarek): If you select Sarek, specify the method (method1 for concatenated or method2 for multilane).
Here is an example of how to run the script:

# Copy code
python fastq_sample_sheet_generator.py
Follow the prompts to input the path and select the appropriate options.

# Output
The script will generate a sample sheet named using the parent directory of the specified fastq directory (interpreted as the run name) and will save this sample sheet in the same directory as the fastq files. An example output file name would be [run_name]_samplesheet.csv.

# Logging
Logs provide detailed information about the script's operations, including errors in input and issues encountered during file handling. Ensure you check the logs if you encounter issues.

# Contact
For any issues or questions, please submit a problem report to the repository or contact the maintainer directly via email.

This README provides the necessary information to get a user started with the script, detailing the functionality, requirements, and execution instructions. Adjust the contact section as needed to provide a way for users to reach out for support.
