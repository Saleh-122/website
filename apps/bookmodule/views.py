from django.shortcuts import render
from .models import signup,car
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
msg = ""
def index(request):
    cars= car.objects.all()
    return render(request, 'bookmodule/index.html', {'cars':cars})

def aboutme(request):
    return render(request, 'bookmodule/aboutme.html')

def signIn(request):
    if request.method == "POST":
        us = request.POST.get('username')
        psw = request.POST.get('psw')
        if signup.objects.filter(userN__exact=us).filter(password__exact=psw):
            cars= car.objects.all()
            return render(request, 'bookmodule/index.html', {'cars':cars})
        else:
            msg = "Error while signing in"
            return render(request, 'bookmodule/error.html',{'message':msg})
        
            
    return render(request, 'bookmodule/signIn.html')

def addCar(request):
    if request.method == "POST":
        n = request.POST.get('name').lower()
        p = request.POST.get('price')
        s = request.POST.get('select')
        
        addC = car(type = s, name=n,price = p)
        addC.save()
        return render(request, 'bookmodule/addCar.html')
        
    
       
    return render(request, 'bookmodule/addCar.html')


def signUp(request):
    if request.method == "POST":
        fn = request.POST.get('fname').lower()
        ln = request.POST.get('lname').lower()
        em = request.POST.get('email').lower()
        us = request.POST.get('username')
        psw = request.POST.get('psw')
        
        if signup.objects.filter(userN__exact=us):
            msg = "The user name you typed is used"
            return render(request, 'bookmodule/error.html',{'message':msg})
            
        elif signup.objects.filter(password__exact=psw):
            msg = "The password you typed is used"
            return render(request, 'bookmodule/error.html',{'message':msg})
        elif signup.objects.filter(email__exact=em):
            msg = "The Email you typed is used"
            return render(request, 'bookmodule/error.html',{'message':msg})
 
    
        else:
            signup1 = signup(firstN = fn, lastN=ln ,email=em,userN=us,password = psw)
            signup1.save()
            cars= car.objects.all()
            return render(request, 'bookmodule/index.html', {'cars':cars})
            
        
    return render(request, 'bookmodule/signUp.html')