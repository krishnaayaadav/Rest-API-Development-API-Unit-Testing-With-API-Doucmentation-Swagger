from django.urls import path
from expenseApp.apiFiles import api_views as exp_apis

urlpatterns = [
    path('expenses/', exp_apis.ExpenseAPIView().as_view(), name='get_or_post_expense'),
    path('expenses/<int:expId>/', exp_apis.ExpenseUpdateAPI().as_view(), name='update_delete_post' ),

]