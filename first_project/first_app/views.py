from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    render_dict = {
        'insert': "see Django is easy!",
    }
    return render(request, 'first_app/index.html', context=render_dict)