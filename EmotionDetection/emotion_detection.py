import requests
import json

def emotion_detector(text_to_analyze):
    """
    Calls IBM Watson Emotion API and returns emotion scores.
    Handles blank input by returning all None values.
    """

    URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # If the user sends blank input, DO NOT call the API — return None values immediately
    if not text_to_analyze or text_to_analyze.strip() == "":
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    # Normal API call
    Input_json = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url=URL, json=Input_json, headers=Headers)

    # --- Required by your instructions: handle status_code = 400 ---
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    # Normal valid 200 response
    formatted_response = json.loads(response.text)
    prediction = formatted_response["emotionPredictions"][0]
    emotion_scores = prediction["emotion"]

    # Determine dominant emotion
    dominant = max(emotion_scores, key=emotion_scores.get)

    return {
        "anger": emotion_scores["anger"],
        "disgust": emotion_scores["disgust"],
        "fear": emotion_scores["fear"],
        "joy": emotion_scores["joy"],
        "sadness": emotion_scores["sadness"],
        "dominant_emotion": dominant
    }
