from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255, name='name')
    amount = models.IntegerField(name='amount')
    description = models.TextField(name='description')