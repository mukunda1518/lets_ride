from django.db import models



class Order(models.Model):

    status = models.CharField(max_length=100)
    shipped_by = models.CharField(max_length=100)
    shipped_on = models.DateTimeField()