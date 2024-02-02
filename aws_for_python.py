import boto3

region = 'your region'

s3 = boto3.resource('s3')

def show_buckets(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)
show_buckets(s3)

#For Uploading files to the S3 Bucket
file_name='Your File Name'       #The name with which the file is stored on your local machine
bucket_name='Your Bucket Name'   ##Name of the Bucket to which the file will be uploaded
key_name='StoredNameInS3Bucket'  #The name with which it will be stored in S3 Bucket

def upload_to_bucket(s3, file_name, bucket_name, key_name):
    print("Uploading file to S3")
    data = open(file_name, 'rb')
    s3.Bucket(bucket_name).put_object(Key=file_name, Body=data)
    print("File uploaded to S3")
upload_to_bucket(s3, file_name, bucket_name, key_name)


#For Downloading files from the S3 Bucket
file_name2='LocalStoredFileName'  #The name with which you want to store the file on your local machine
bucket_name2='Name of the Bucket' #Name of the Bucket from which the file will be downloaded
key_name2='StoredNameInS3Bucket'  #Actual name of the file that needs to be downloaded

def download_from_bucket(s3, file_name2, bucket_name2, key_name2):
    print("Downloading file from S3")
    s3.Bucket(bucket_name2).download_file(key_name2, file_name2)
    print("File downloaded from S3")
download_from_bucket(s3, file_name2, bucket_name2, key_name2)
