from django.urls import path
from . import views
from speech_to_text.views import *


urlpatterns = [
    path('', index),
]