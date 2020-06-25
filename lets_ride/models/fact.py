from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100)

class User1(models.Model):
    first_name = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)




class User2(models.Model):
    name = models.CharField(max_length=100)


class UserLog(models.Model):
    user = models.ForeignKey(User2, on_delete=models.CASCADE)
    action = models.CharField(max_length=100)






class Group1(models.Model):
    name = models.CharField(max_length=100)

class User3(models.Model):
    name = models.CharField(max_length=100)
    groups = models.ManyToManyField(Group1)







class User4(models.Model):
    name = models.CharField(max_length=100)

class Group4(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User4, through='GroupLevel')

class GroupLevel(models.Model):
    user = models.ForeignKey(User4, on_delete=models.CASCADE)
    group = models.ForeignKey(Group4, on_delete=models.CASCADE)
    rank = models.IntegerField()



class Country(models.Model):
    name = models.CharField(max_length=100)
    lang = models.CharField(max_length=100)

class User5(models.Model):
    name = models.CharField(max_length=100)
    lang = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

# class Organization(models.Model):
#     name = models.CharField(max_length=100)
#     country = models.ForeignKey(Country, on_delete=models.CASCADE)

class Company(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User5, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    #organization = models.ForeignKey(Organization, on_delete=models.CASCADE)


class User6(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

# class User6(models.Model):
#     name = models.CharField(max_length=100)


# class Post(models.Model):
#     name = models.CharField(max_length=100)
#     user = models.ForeignKey(User6, on_delete=models.CASCADE)