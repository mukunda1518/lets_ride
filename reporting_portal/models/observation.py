from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    profile_pic = models.TextField()
    role = models.CharField(max_length=100, default="user")

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


class Observation(models.Model):
    title = models.CharField(max_length=100)
    repoted_on = models.DateTimeField(auto_now_add=True)
    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.CASCADE,
        null=True
    )
    description = models.TextField()
    severity = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default="REPORTED")
    due_date = models.DateTimeField()
    repoted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)


class Attachments(models.Model):
    url = models.TextField()
    observation = models.ForeignKey(Observation, on_delete=models.CASCADE)

class Messages(models.Model):
    observation = models.ForeignKey(Observation, on_delete=models.CASCADE)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)