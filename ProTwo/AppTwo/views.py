from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<em> My Second Application</em>')

def help(request):
    
    my_response_template = {
        "insertContent":"Help me!"
    }
    
    return render(request,"AppTwo/help.html",my_response_template)