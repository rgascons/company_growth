from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=50)
    ticker = models.CharField(max_length=15)
    country = models.CharField(max_length=5, default="Unknown")
    stock_exchange = models.CharField(max_field=5, default="Unknown")
    current_price = models.FloatField()
    last_earnings = models.FloatField()
    earnings_increase = models.FloatField()
