from django.shortcuts import render

def index(request):
    return render(request, 'bookmodule/index.html')

def aboutme(request):
    return render(request, 'bookmodule/aboutme.html')

def signIn(request):
    return render(request, 'bookmodule/signIn.html')

def signUp(request):
    return render(request, 'bookmodule/signUp.html')