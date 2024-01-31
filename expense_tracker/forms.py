from django.forms import forms

from expense_tracker.models import User


class ExpenseForm(forms.Form):
    total_amount = forms.DecimalField()
    participants = forms.ModelMultipleChoiceField(queryset=User.objects.all())
