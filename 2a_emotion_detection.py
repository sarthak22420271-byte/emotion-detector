import requests

def emotion_detector(text_to_analyze):
    """
    This function sends text to Watson NLP Emotion API
    and returns the detected emotions.
    """

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    json_data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, json=json_data, headers=headers)

    # Return raw JSON if successful
    if response.status_code == 200:
        return response.json()
    else:
        return None
