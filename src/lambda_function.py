import os
import json
from transformers import pipeline

def lambda_handler(event, context):
    # using pipeline API for summarization task
    summarization = pipeline("summarization")
    # Get the input text from Lambda event
    input_text = event['input_text']

    summary_text = summarization(input_text)[0]['summary_text']

    return {
        "statusCode" : 200,
        "summary" : summary_text
    }

if __name__ == '__main__':
    print(lambda_handler(event={'input_text' : "Hello world, this is a test summarization tool."}, context=''))