import os
import json
from happytransformer import HappyTextToText, TTSettings

# Manually call save_model to overwrite the `model` folder before uploading to AWS
def save_model():
    model = HappyTextToText(model_type="BART", model_name="facebook/bart-large-cnn")
    model.save("model/")

def lambda_handler(event, context):
    # Load model during function initialization
    model = HappyTextToText(model_type="BART", model_name="model/")

    # Get the input text from Lambda event
    input_text = event['input_text']

    # Summarization settings
    summary_args = TTSettings(min_length=1, max_length=500)

    # Generate the summary
    result= model.generate_text(input_text, summary_args)

    return {
        "statusCode" : 200,
        "summary" : result.text
    }

if __name__ == '__main__':
    save_model()
    print(lambda_handler())