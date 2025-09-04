import requests
import json
def emotion_detector(text_to_analyze):
    # API endpoint and headers
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
        # Input JSON
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }  
    # Send POST request
    response = requests.post(url, headers=headers, json=input_json)
    result=json.loads(response.text)
    emotions = result['emotionPredictions'][0]['emotion']
      # Extract required emotions
    anger = emotions.get('anger', 0)
    disgust = emotions.get('disgust', 0)
    fear = emotions.get('fear', 0)
    joy = emotions.get('joy', 0)
    sadness = emotions.get('sadness', 0)
    # Find dominant emotion
    emotion_scores = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness
    }
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }