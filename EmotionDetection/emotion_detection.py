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

    if response.status_code == 400:
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}

    # Parse the response from the API
    response_text = json.loads(response.text)

    # Extract the emotion scores, find the dominant emotion, and pack it in a dictionary
    emotions = response_text['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions, key=emotions.get)
    formatted_emotions = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }

    return  formatted_emotions

if __name__ == "__main__":
    # Ask for user input interactively
    text = input("Enter the text to analyze: ")
    emotions = emotion_detector(text)
    print(json.dumps(emotions, indent=4))
