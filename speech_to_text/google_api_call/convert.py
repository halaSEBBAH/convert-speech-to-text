import io
import os

# Imports the Google Cloud client library
from google.cloud import speech

### to indicate the api key
credential_path = "Your google api path.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path


def convert_to_text(audio):

    text = ""    
    try:
        client = speech.SpeechClient()

        content = audio.read()
        audio = speech.RecognitionAudio(content=content)

        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code="en-US",
        )
        
        response = client.recognize(config=config, audio=audio)
        for result in response.results:
            text= text+ "{}".format(result.alternatives[0].transcript)
    except:
        text = "we are sorry, there has been w problem , please check your credentials and retry"


    return text
