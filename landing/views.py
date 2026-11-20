from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
            "name":"bulongo",
            "age": 37,
            "occupation": "programmer"
            }
    return render(request,"landing/index.html",context)
