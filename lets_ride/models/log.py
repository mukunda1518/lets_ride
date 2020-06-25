from django.db import models

class Log(models.Model):

    timestamp = models.DateTimeField()
