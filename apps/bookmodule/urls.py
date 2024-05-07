
from django.urls import path, include
from apps.bookmodule import views

urlpatterns = [
    path('index',views.index),
    path('aboutme',views.aboutme),
    path('signIn',views.signIn),
    path('signUp',views.signUp),
    path('addCar',views.addCar),
     
    
]



