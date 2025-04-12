import boto3

s3_client = boto3.client('s3')

def list_buckets():
    try:
        response = s3_client.list_buckets()
        print("S3 Buckets in your account:")
        for bucket in response['Buckets']:
            print(f"- {bucket['Name']}")
    except Exception as e:
        print(f"Error listing buckets: {str(e)}")

def count_objects_in_bucket(bucket_name):
    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in response:
            total_objects = len(response['Contents'])
            print(f"Total number of objects in bucket '{bucket_name}': {total_objects}")
        else:
            print(f"The bucket '{bucket_name}' is empty or inaccessible.")
    except Exception as e:
        print(f"Error counting objects in bucket {bucket_name}: {str(e)}")

if __name__ == "__main__":
    list_buckets()

    bucket_name = input("Enter the name of the S3 bucket to count objects: ")
    count_objects_in_bucket(bucket_name)

