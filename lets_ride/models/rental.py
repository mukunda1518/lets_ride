from django.db import models

class Rental(models.Model):

    begin = models.DateTimeField()
    end = models.DateTimeField()