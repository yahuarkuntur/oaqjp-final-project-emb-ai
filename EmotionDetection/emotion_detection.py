import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json={ "raw_document": { "text": text_to_analyze }}, headers=headers)
    emotions_data = json.loads(response.text)

    emotion_keys = ("anger", "disgust", "fear", "joy", "sadness")
    return_data = {}
    highest_score = 0
    dominant_emotion = None

    for key in emotion_keys:
        score = emotions_data["emotionPredictions"][0]["emotion"][key]
        return_data[key] = score
        if score >= highest_score:
            highest_score = score
            dominant_emotion = key

    return_data["dominant_emotion"] = dominant_emotion

    return return_data