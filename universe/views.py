from datetime import datetime

from django.shortcuts import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse("Hello! It's my project")

def now_date(request):
    current_date = datetime.now()
    response = HttpResponse(current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return response

def goodbye(request):
    return HttpResponse("Goodbye user!")

