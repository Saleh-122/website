
from django.urls import path, include
from apps.bookmodule import views

urlpatterns = [
    path('',views.index,name='index'),
    path('aboutme',views.aboutme),
    path('signIn',views.signIn),
    path('signUp',views.signUp),
    
]



