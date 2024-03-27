from django.shortcuts import render

def index(request):
    return render(request, 'bookmodule/index.html')

def aboutme(request):
    return render(request, 'bookmodule/aboutme.html')