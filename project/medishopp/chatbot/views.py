from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json
from .chatbott import chat_with_bot

@csrf_exempt                                                                
def chat_api(request):
    if request.method == "POST":
        data = json.loads(request.body)
        message = data.get("message", "")
        response = chat_with_bot(message)
        return JsonResponse({"response": response})
    return JsonResponse({"error": "Only POST allowed"})                             

def chat_page(request):                     
    return render(request, "chatbot.html")
                                 