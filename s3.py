import boto3

# Creating Session With Boto3.
session = boto3.Session(
    aws_access_key_id='<your_access_key_id>',
    aws_secret_access_key='<your_secret_access_key>'
)

# Creating S3 Resource From the Session.
s3 = session.resource('s3')

txt_data = b'This is the content of the file uploaded from python boto3 asdfasdf'

object = s3.Object('<bucket_name>', './download.jfif')

result = object.put(Body=txt_data)
