from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'web/top_spots.html',{})
    # return HttpResponse("nigger we made it")