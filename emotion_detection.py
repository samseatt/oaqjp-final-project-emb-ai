import requests, json

def emotion_detector(text_to_analyze):

    # Define the URL for the emotion detection/prediction API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    # Parse the response from the API
    formatted_response = json.loads(response.text)

    return formatted_response

if __name__ == "__main__":
    # Ask for user input interactively
    text = input("Enter the text to analyze: ")
    result = emotion_detector(text)
    print(f"Detected emotion: {result}")
