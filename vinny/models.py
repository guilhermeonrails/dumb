from django.db import models

class Frase(models.Model):
    author = models.CharField(max_length=300)
    text = models.CharField(max_length=1000)
