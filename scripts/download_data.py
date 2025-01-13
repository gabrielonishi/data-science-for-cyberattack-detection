'''
This script downloads a specific file from the CSE-CIC-IDS2018 dataset from AWS S3.

Sources that inspired this script:
 - https://www.unb.ca/cic/datasets/ids-2018.html
 - https://registry.opendata.aws/cse-cic-ids2018/
'''
import shutil
import os
import subprocess


def check_aws_cli():
    """Check if AWS CLI is installed."""
    aws_cli = shutil.which("aws")
    if aws_cli is None:
        print("AWS CLI is not installed. Please install it to proceed.")
    print("AWS CLI is installed.")

def check_if_file_exists(file_path):
    if os.path.exists(file_path):
        print(f"File {file_path} already exists.")
        return True

def download_data():
    """Download a specific file from S3 using AWS CLI."""
    s3_url = 's3://cse-cic-ids2018/'
    target_folder_path = 'Processed Traffic Data for ML Algorithms/'
    target_file_path = 'Wednesday-14-02-2018_TrafficForML_CICFlowMeter.csv'
    dest_dir = "data/raw"
    command = f'aws s3 cp --no-sign-request "{s3_url + target_folder_path + target_file_path}" {dest_dir}'
    
    file_exists = check_if_file_exists(f"{dest_dir}/{target_file_path}")
    
    if file_exists:
        return

    try:
        print(command)
        os.system(command)
        print("File downloaded successfully!")
    except subprocess.CalledProcessError as e:
        print("An error occurred while downloading the file.")
        print(e)
        
if __name__ == '__main__':
    check_aws_cli()
    download_data()