from rest_framework.serializers import ModelSerializer

from expense_tracker.models import User, Expense


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ExpenseSerializer(ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'
