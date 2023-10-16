from django.urls import path
from expenseApp.apiFiles import api_views as exp_apis

urlpatterns = [
    # Expense API Endpoints
    path('expense/',     exp_apis.ExpenseListAPIView.as_view(), name='get_all_expenses' ),
    path('expense/add/', exp_apis.ExpensePostAPI.as_view(),     name='add_new_expense'),
    path('expense/search/<str:search_by>/', exp_apis.ExpenseSearchAPI.as_view(), name='expense_search_api'),
    path('expense/details/<int:expId>/', exp_apis.ExpenseDetailAPI.as_view(), name='get_expense_detail'),
    path('expense/update/<int:expId>/',  exp_apis.ExpenseUpdateAPI.as_view(), name='expense_update_api'),
    path('expense/delete/<int:expId>/',  exp_apis.ExpenseDeleteAPI.as_view(), name='expense_delete_api')


]