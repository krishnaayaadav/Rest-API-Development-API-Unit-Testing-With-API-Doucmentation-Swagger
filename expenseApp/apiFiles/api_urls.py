from django.urls import path
from expenseApp.apiFiles import api_views as exp_apis

urlpatterns = [
    path('expenses/', exp_apis.ExpenseAPIView().as_view()),
]