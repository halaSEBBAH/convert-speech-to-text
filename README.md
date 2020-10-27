## Web speech to text converter

A web page to convert audio files to written text using google api


### Prerequisites

Django version : 2.0.3



### Google speech 
using the library and the instuctiong described here  https://cloud.google.com/speech-to-text/docs/libraries



### How to run project
*set python virtual environement
•	Run command python -m venv C:\path to my folder 
•	Navigate to C:\path to my folder\Scripts and run activate
•	Run pip install Django
•	Run pip install django-cors-headers
•	Run pip install google-cloud-speech
* set google credentials in speech_to_text\google_api_call\convert.py   
* naviagate to speech_to_text
* run python manage.py migrate 
* run python manage.py runserver





