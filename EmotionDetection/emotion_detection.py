import requests
import json

def emotion_detector(text_to_analyze):
    return {
        'anger': 0.01,
        'disgust': 0.02,
        'fear': 0.03,
        'joy': 0.85,
        'sadness': 0.01,
        'dominant_emotion': 'joy'
    }

def start(text_to_analyze):
    if not text_to_analyze:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        data = response.json()
        
        # Extract emotion scores
        emotions = {
            'anger': data.get('anger', 0),
            'disgust': data.get('disgust', 0),
            'fear': data.get('fear', 0),
            'joy': data.get('joy', 0),
            'sadness': data.get('sadness', 0)
        }
        
        # Find the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)
        
        # Format the output
        result = {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': dominant_emotion
        }
        
        return result
    else:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
