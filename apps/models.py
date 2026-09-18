from django.db import models
from django.db.models import Model, ForeignKey, CASCADE
from django.db.models.fields import CharField, PositiveIntegerField, DecimalField


# Create your models here.
class Category(Model):
    title = CharField(max_length=255)
    


class Product(Model):
    title = CharField(max_length=255)
    category = ForeignKey('apps.Category', on_delete=CASCADE, related_name='products')
    stock = PositiveIntegerField()
    price = DecimalField(max_digits=12, decimal_places=0)

