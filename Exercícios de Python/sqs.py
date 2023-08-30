import boto3

# Get the SQS client.
sqs_client = boto3.client('sqs')

# Create a queue.
queue_name = 'fila'
queue_url = sqs_client.create_queue(QueueName=queue_name)['https://sqs.us-east-1.amazonaws.com/619180032002/fila']

# Send a message to the queue.
message_body = 'This is a message.'
sqs_client.send_message(QueueUrl=queue_url, MessageBody=message_body)

# Receive a message from the queue.
messages = sqs_client.receive_message(QueueUrl=queue_url)

# Get the message body.
message_body = messages[0]['Body']

# Print the message body.
print(message_body)
