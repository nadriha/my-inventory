from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    name = models.CharField(max_length=255, name='name')
    amount = models.IntegerField(name='amount')
    description = models.TextField(name='description')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
