import json

def lambda_handler(event, context):
    print("🔔 S3 Event Triggered:")
    print(json.dumps(event, indent=2))
    return {
        'statusCode': 200,
        'body': json.dumps('Event logged to CloudWatch!')
    }

