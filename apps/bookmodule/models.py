
from django.db import models


class signup(models.Model):
    firstN = models.CharField(max_length = 20)
    lastN = models.CharField(max_length = 20)
    email = models.CharField(max_length = 50)
    userN = models.CharField(max_length = 5)
    password = models.CharField(max_length = 14)
    
class car(models.Model):
    
    type = models.CharField(max_length = 20)
    name = models.CharField(max_length = 50)
    price = models.IntegerField()
     
    
 

