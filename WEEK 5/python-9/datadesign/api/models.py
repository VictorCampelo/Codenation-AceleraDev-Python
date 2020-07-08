from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    last_login = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length = 254)
    password = models.CharField(max_length=50)
    objects = models.Manager()


class Agent(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    status = models.BooleanField()
    env = models.CharField(max_length=20)
    version = models.CharField(max_length=5)
    address = models.GenericIPAddressField(protocol="IPV4", default="0.0.0.0")
    objects = models.Manager()

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    level = models.CharField(max_length=20)
    data = models.TextField()
    arquivado = models.BooleanField()
    date = models.DateField(auto_now=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()

class Group(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    objects = models.Manager()
    
class GroupUser(models.Model):
    id = models.AutoField(primary_key=True)
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    objects = models.Manager()