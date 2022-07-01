from django.db import models
from django.forms import CharField

# Create your models here.
class Topic(models.Model):
    typetopic=models.CharField(max_length=255,null=False,)