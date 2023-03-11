import boto3


s3 = boto3.resource('s3')

c = 0
for bucket in s3.buckets.all():
    print(bucket)
    c = c+1

s3.Bucket ("jenkins-servers").download_file("download.png","download.png")    