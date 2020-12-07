from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse
import json
import requests


# Create your views here.
def login(request):
    return render(request, 'login.html')

class Home(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        data = request.POST['message']
        response = self.getResponse(data)
        return JsonResponse({"ques":data, "res":response})
        
    def getResponse(self, question):
        data=json.dumps({"message":"%s"%question, "sender":"Me"})
        p = requests.post('http://localhost:5005/webhooks/rest/webhook', headers={"Content-Type": "application/json"},data=data).json()
        try:
            return p[0]['text']
        except :
            return "đéo hiểu"
        
