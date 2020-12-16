from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse
import json
import requests
from . import models
from datetime import datetime
from tensorflow.keras.models import load_model
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


# Create your views here.

path = models.ModelThemDau.objects.get(id = 1).model_h5.path
model = load_model(path)


def getResponse(question):
    data = json.dumps({"message": "%s" % question, "sender": "Me"})
    p = requests.post('http://localhost:5005/webhooks/rest/webhook',
                        headers={"Content-Type": "application/json"}, data=data).json()
    try:
        return p[0]['text']
    except:
        return "không hiểu"

class Home(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        data = request.POST['message']
        response = getResponse(data)
        if "không hiểu" not in response:
            timeID = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            chat = models.ChatContent(
                timeID=timeID, question=data, response=response)
            chat.save()
        return JsonResponse({"ques": data, "res": response})


def get_chat_content(request):
    chat = models.ChatContent.objects.all()
    return render(request, 'chat_content.html', {'chat': chat})





        