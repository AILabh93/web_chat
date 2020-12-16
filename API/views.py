from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from chat import views
from . import them_dau

 
# Create your views here.
class APIThemDau(APIView):
    
    def post(self, request):
        try:
            data = request.data
            text = data['text']
            text = them_dau.accent_sentence(text, views.model)
            print(text)
            text = views.getResponse(text)
            return Response(data={'text':text}, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        