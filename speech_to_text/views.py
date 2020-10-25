from django.shortcuts import render
from .google_api_call.convert import convert_to_text
import requests

def index(request):
    
    text = []

    if request.method == 'POST' and request.FILES['document']:
        
        uploaded_file = request.FILES['document']
        
        response = convert_to_text(uploaded_file)

        for result in response.results:
            text.append("Le text est: {}".format(result.alternatives[0].transcript))


    context = {'text' : text}
    return render(request, 'page.html', context)
