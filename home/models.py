# models.py
from django.db import models
from django.contrib.auth.models import User

class Sales(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.AutoField(primary_key=True)
    product = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    customer_name = models.CharField(max_length=100)
    order_date = models.DateTimeField(auto_now_add=True)
    receipt_img = models.ImageField(upload_to='receipts/')

    def __str__(self):
        return f"{self.product} ordered by {self.customer_name}"
