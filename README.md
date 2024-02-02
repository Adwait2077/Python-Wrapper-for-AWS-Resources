# Python Wrapper for AWS S3

This Python project offers a convenient wrapper for interacting with AWS S3, simplifying file upload and download operations.

## Features

- **Upload to S3:** Easily upload files to an AWS S3 bucket.
- **Download from S3:** Download files from an AWS S3 bucket to your local machine.

## Usage

1. Clone the repository:
   https://github.com/Adwait2077/Python-Wrapper-for-AWS-Resources.git

2. Install the required dependencies:
   pip install -r requirements.txt

3. Open the script and replace the placeholder values with your AWS credentials and specific details.

4. Run the script:
    python your_script_name.py

## Dependencies

- [boto3](https://github.com/boto/boto3) - The Amazon Web Services (AWS) SDK for Python.

# Replace with your actual AWS credentials and details
region = 'your_region'
s3 = boto3.resource('s3')
file_name = 'YourFileName.txt'
bucket_name = 'YourBucketName'
key_name = 'StoredNameInS3Bucket.txt'

## Explanation:

- The function starts by providing a list of buckets available in the Amazon S3 service.
-Then the function starts by printing a message indicating that the file is being uploaded to S3.
-It then opens the specified local file (file_name) in binary read mode ('rb'). The file content is read into the data variable.
-Using the S3 resource (s3), it accesses the specified bucket (bucket_name) and uses the put_object method to upload the file. The Key parameter is set to the specified key_name, and the file content is set as the Body.
-After the file is successfully uploaded, a message is printed indicating that the file has been uploaded to S3.

Similarly for Downloading:
-The function initiates the process by printing a message indicating that the file is being downloaded from Amazon S3.
-It then uses the S3 resource (s3) to access the specified S3 bucket (bucket_name2).
-The download_file method is called to download the file specified by key_name2 from the S3 bucket. The downloaded file is saved locally with the name file_name2.
-Once the file is successfully downloaded, a message is printed, indicating that the file has been downloaded from S3.
