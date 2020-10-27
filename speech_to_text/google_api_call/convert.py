import io
import os

# Imports the Google Cloud client library
from google.cloud import speech

### to indicate the api key
credential_path = "C:\\Users\\hala\\Documents\\Ma formation\My Project-b17003affe03.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path


def convert_to_text(audio):

    client = speech.SpeechClient()

    content = audio.read()
    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )
    
    response = client.recognize(config=config, audio=audio)

    return response
