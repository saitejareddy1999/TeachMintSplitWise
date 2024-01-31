from django.urls import path, include
from rest_framework.routers import DefaultRouter


from expense_tracker.views import add_expense, add_expense2, add_expense3
from expense_tracker.views import UserViewSet

router = DefaultRouter()
router.register('', UserViewSet)
# router.register('add_expense/',AddExpenseView)

urlpatterns = [
    path('', include(router.urls)),
    path('add_expense/', add_expense, name='add_expense'),
    path('add_expense2/', add_expense2, name='add_expense2'),
    path('add_expense3/', add_expense3, name='add_expense3'),

    # path('add_expense/', AddExpenseView.as_view({'post': 'create'}), name='add-expense'),
]
