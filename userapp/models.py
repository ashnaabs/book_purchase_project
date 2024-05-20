from django.contrib.auth.models import User
from django.db import models
from my_app.models import Book
# Create your models here.


class Cart(models.Model):           #creating model cart (user and items)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='cart_items')
    items=models.ManyToManyField(Book)

class Cartitem(models.Model):           #model cart items(joining book,quantity and cart)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)