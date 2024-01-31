from enum import Enum

from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10, default=True)

    # email = models.EmailField(unique=True)
    # mobile_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name


# class ExpenseTypes(Enum):
#     EQUAL = 'EQUAL'
#     EXACT = 'EXACT'
#     PERCENT = 'PERCENT'


class Expense(models.Model):
    # type = models.CharField(max_length=25, choices=[(e.name, e.value) for e in ExpenseTypes], blank=True)
    payer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='paid_expenses')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    participants = models.ManyToManyField(User, related_name='shared_expenses')

    def __str__(self):
        return f"participants: {self.participants} Expense:{self.total_amount}"


class Expense2(models.Model):
    payer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='paid_expenses1')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    participants = models.ManyToManyField(User, related_name='shared_expenses1')
    exact_amounts = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"participants: {self.participants} Expense:{self.total_amount}"


class Expense3(models.Model):
    payer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='paid_expenses2')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    participants = models.ManyToManyField(User, related_name='shared_expenses2')
    exact_amounts = models.DecimalField(max_digits=5, decimal_places=2, blank=True)

    def __str__(self):
        return f"participants: {self.participants} Expense:{self.total_amount}"
# class ExpenseParticipate(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
#     amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
#
#     def __str__(self):
#         return f"{self.user.name} - {self.expense.type} Expense: {self.amount_paid}"
