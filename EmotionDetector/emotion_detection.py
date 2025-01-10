import requests, json  # Import the requests library to handle HTTP requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        predictions = formatted_response.get('emotionPredictions', [])
        if predictions:
            emotion_data = predictions[0].get('emotion', {})
            return emotion_data
        else:
            return {'error': 'No predictions found'}
    else:
        return {'error': response.status_code}
