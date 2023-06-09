from django.db import models


class User(models.Model):
    name = models.CharField(max_length=80)
    password = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
