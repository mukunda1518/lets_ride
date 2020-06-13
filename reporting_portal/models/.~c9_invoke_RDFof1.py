from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    profile_pic = models.TextField()
    role = models.CharField(max_length=100)

class Category(models.Model):
    name = models.CharField(max_length=100)


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE,
        related_name="subcategories"
    )
    rp = models.OneToOneField(User, on_delete=models.CASCADE)

class Attachments(models.Model):
    url = models.TextField()

    
class Observation(models.Model):
    title = models.CharField(max_length=100)
    repoted_on = models.DateTimeField(auto_now_add=True)
    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.CASCADE,
        null=True
    )
    
    