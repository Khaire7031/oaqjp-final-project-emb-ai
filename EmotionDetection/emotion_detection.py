import requests
import json

def emotion_detector(text):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_API_KEY"  # Replace with your actual API key
    }
    
    if not text:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    payload = {
        "text": text
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 400:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
        response_data = response.json()
        anger_score = response_data.get('anger', 0)
        disgust_score = response_data.get('disgust', 0)
        fear_score = response_data.get('fear', 0)
        joy_score = response_data.get('joy', 0)
        sadness_score = response_data.get('sadness', 0)
        
        emotions = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        
        dominant_emotion = max(emotions, key=emotions.get)
        
        return {
            **emotions,
            'dominant_emotion': dominant_emotion
        }
    except Exception as e:
        print(f"An error occurred: {e}")
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
