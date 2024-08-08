
from django.db import models

class Expense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.FloatField()
    date = models.DateField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Budget(models.Model):
    name = models.CharField(max_length=100)
    amount = models.FloatField()

    def __str__(self):
        return self.name

class FinancialGoal(models.Model):
    name = models.CharField(max_length=100)
    target_amount = models.FloatField()
    saved_amount = models.FloatField()

    def __str__(self):
        return self.name
