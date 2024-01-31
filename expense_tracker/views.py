from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from requests import Response
from rest_framework import viewsets, status, permissions

from expense_tracker.models import User, Expense
from expense_tracker.serializers import UserSerializer, ExpenseSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


# example 1
def add_expense(request):
    if request.method == 'POST':
        payer_id = request.POST.get('payer_id')
        total_amount = request.POST.get('total_amount')
        participants_ids = request.POST.getlist('participants_ids[]')

        payer = User.objects.get(id=payer_id)
        participants = User.objects.filter(id__in=participants_ids)

        expense = Expense.objects.create(payer=payer, total_amount=total_amount)
        expense.participants.add(*participants)

        each_share = float(total_amount) // (len(participants))
        payer.balance -= each_share
        payer.save()
        for participant in participants:
            participant.balance += each_share
            participant.save()

        return JsonResponse({'message': 'Expense added successfully'}, status=201)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


# Example:2

def add_expense2(request):
    if request.method == 'POST':
        payer_id = request.POST.get('payer_id')
        total_amount = request.POST.get('total_amount')
        participants_ids = request.POST.getlist('participants_ids[]')
        exact_amounts = request.POST.getlist('exact_amounts[]')  # New field for exact amounts

        payer = User.objects.get(id=payer_id)
        participants = User.objects.filter(id__in=participants_ids)

        expense = Expense.objects.create(payer=payer, total_amount=total_amount)
        expense.participants.add(*participants)

        payer.balance -= float(total_amount)
        payer.save()

        for idx, participant in enumerate(participants):
            exact_amount = float(exact_amounts[idx])
            participant.balance += exact_amount
            participant.save()

        return JsonResponse({'message': 'Expense added successfully'}, status=201)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


# Example 3
def add_expense3(request):
    if request.method == 'POST':
        payer_id = request.POST.get('payer_id')
        total_amount = float(request.POST.get('total_amount'))
        participants_ids = request.POST.getlist('participants_ids[]')
        percentages = [float(percentage) for percentage in request.POST.getlist('percentages[]')]

        payer = User.objects.get(id=payer_id)
        participants = User.objects.filter(id__in=participants_ids)

        #  individual shares for  percentages
        total_percentage = sum(percentages)
        shares = [total_amount * percentage / 100 for percentage in percentages]

        expense = Expense.objects.create(payer=payer, total_amount=total_amount)
        expense.participants.add(*participants)

        for participant, share in zip(participants, shares):
            participant.balance -= share
            participant.save()
            payer.balance += share

        payer.balance -= total_amount
        payer.save()

        return JsonResponse({'message': 'Expense added successfully'}, status=201)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
