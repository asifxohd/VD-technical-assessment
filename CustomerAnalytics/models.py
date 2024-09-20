# models.py
from django.db import models
from django.utils import timezone
from django.db.models import Sum
from datetime import timedelta

class Customer(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    status = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    @classmethod
    def top_customers(cls):
        six_months_ago = timezone.now() - timedelta(days=180)
        return (
            cls.objects.filter(order_date__gte=six_months_ago)
            .values('customer__name')
            .annotate(total_spent=Sum('total_amount'))
            .order_by('-total_spent')[:5]
        )
