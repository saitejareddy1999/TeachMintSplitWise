from django.test import TestCase, Client
from django.urls import reverse
from expense_tracker.models import User


class AddExpenseViewTestCase(TestCase):
    def setUp(self):
        # Create test users
        self.payer = User.objects.create(name='saitejareddy', balance=1000)
        self.participant1 = User.objects.create(name='Raghupathireddy', balance=1000)
        self.participant2 = User.objects.create(name='U3', balance=1000)

    def test_add_expense(self):
        client = Client()

        # Prepare request data
        data = {
            'payer_id': self.payer.id,
            'total_amount': 1000,
            'participants_ids[]': [self.participant1.id, self.participant2.id]
        }

        # Send POST request to add_expense endpoint
        response = client.post(reverse('add_expense'), data=data)

        # Check if the response is as expected
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'message': 'Expense added successfully'})

        # Check if balances are updated correctly
        self.payer.refresh_from_db()
        self.participant1.refresh_from_db()
        self.participant2.refresh_from_db()
        self.assertEqual(self.payer.balance, 667)
        self.assertEqual(self.participant1.balance, 1333)
        self.assertEqual(self.participant2.balance, 1333)
