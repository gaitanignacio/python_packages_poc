import logging
import boto3
from botocore.exceptions import ClientError
from boto3.s3.transfer import TransferConfig


DEFAULT_BUCKET_NAME='awspythonsdktest'


class aws_handler():
    def __init__(self, bucketname = DEFAULT_BUCKET_NAME):
        self.bucket = bucketname
        self.s3_client = boto3.client('s3')
        self.config = TransferConfig(multipart_threshold=5*1024 , max_concurrency=5) # 5MB & 5 threads

    def upload_file(self, file_name, object_name=None):

        # If S3 object_name was not specified, use file_name
        if object_name is None:
            object_name = file_name

        # Upload the file
        try:
            response = self.s3_client.upload_file(file_name,
                                                self.bucket,
                                                object_name,
                                                ExtraArgs={'Metadata': {'session_id': 'myvalue'}},
                                                Config=self.config)

        except ClientError as e:
            logging.error(e) # TODO JOIN THE GENERAL LOGGING
            return False
        return True

    def download_file(self, file_name, object_name=None):

        # If S3 object_name was not specified, use file_name
        if object_name is None:
            object_name = file_name

        # Upload the file
        try:
            response = self.s3_client.download_file(self.bucket,
                                        object_name,
                                        file_name,
                                        Config=self.config)
        except ClientError as e:
            logging.error(e)
            return False
        return True

    def upload_fileobj(self, file_name, object_name=None):
        # If S3 object_name was not specified, use file_name
        if object_name is None:
            object_name = file_name
        
        with open(file_name, "rb") as f:
            self.s3_client.upload_fileobj(f, 
                                        self.bucket, 
                                        object_name,
                                        ExtraArgs={'Metadata': {'session_id': 'myvalue'}},
                                        Config=self.config)
    
    def download_fileobj(self, file_name, object_name=None):
        if object_name is None:
            object_name = file_name
   
        with open(file_name, 'wb') as f:
            self.s3_client.download_fileobj(self.bucket, object_name, f, Config=self.config)

# INTSTANTIATE HANDLER AND UPLOAD

aws = aws_handler()
aws.upload_file('info.log','info.log')


# TO CHECK FOR ALL FILES ON BUCKET

paginator = aws.s3_client.get_paginator('list_objects_v2')
page_iterator = paginator.paginate(Bucket='awspythonsdktest')
for bucket in page_iterator:
    for file in bucket['Contents']:
        print(file['Key'])
        try:
            metadata = aws.s3_client.head_object(Bucket='awspythonsdktest', Key=file['Key'])
            print(metadata)
        except:
            print("Failed {}".format(file['Key']))


# TO GET THE METADATA

metadata = aws.s3_client.head_object(Bucket='awspythonsdktest', Key='info.log')
print(metadata['Metadata']['session_id'])