from django.db import models

# Create your models here.

# class ChatContent(models.Model):

class ChatContent(models.Model):
    timeID = models.CharField(max_length = 50)
    question = models.CharField(max_length = 200)
    response = models.CharField(max_length = 200)


class ModelThemDau(models.Model):
    model_h5 = models.FileField(upload_to='model')
