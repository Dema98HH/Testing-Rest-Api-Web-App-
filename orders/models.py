from email.policy import default
from random import choices
from django.db import models
from django.contrib.auth import get_user_model
from django_filters import FilterSet
from django_filters import rest_framework as filters



from authentication.models import User

# Create your models here.

User = get_user_model()


class Order(models.Model):

    SIZES = (
        ('SMALL', 'small'),
        ('MEDIUM', 'medium'),
        ('LARGE', 'large'),
        ('EXTRA_LARGE', 'extraLarge')
    )

    ORDER_STATUS = (
        ('PENDUNG', 'pending'),
        ('PEIN_TRANSIT', 'inTransit'),
        ('DELIVERED', 'delivered')
    )

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    size = models.CharField(max_length=20, choices=SIZES, default=SIZES[0][0])
    order_status = models.CharField(max_length=20, choices=ORDER_STATUS, default=ORDER_STATUS[0][0])
    quantiny = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<Order {self.size} by {self.customer.id}>"
        

class UserFilter(FilterSet):
    class Meta:
        model = Order
        fields = ['size']