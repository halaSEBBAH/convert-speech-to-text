from django.shortcuts import render
from .google_api_call.convert import convert_to_text
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework.response import Response


@csrf_exempt
def index(request):
    return render(request, 'home.html')



@csrf_exempt
def ajax_responce(request):

    text = ""

    if request.method == 'POST' and bool(request.FILES):
        uploaded_file = request.FILES['document']       
        response = convert_to_text(uploaded_file)
        for result in response.results:
            text= text+ "{}".format(result.alternatives[0].transcript)

    responce = {'msg' : text}

    return JsonResponse(responce) 

