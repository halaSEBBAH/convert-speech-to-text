from django.urls import path
from . import views
from speech_to_text.views import *


urlpatterns = [
    path('', index),
    path('ajax-posting/', ajax_responce, name='ajax_posting'),# ajax-posting / name = that we will use in ajax url
]