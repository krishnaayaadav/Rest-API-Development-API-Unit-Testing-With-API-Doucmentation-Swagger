from expenseApp.models import Expense
from expenseApp.apiFiles import serializers as exp_serializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

ok_restponse = status.HTTP_200_OK
created      = status.HTTP_201_CREATED
not_found    = status.HTTP_404_NOT_FOUND
bad_request  = status.HTTP_400_BAD_REQUEST


class ExpenseAPIView(APIView):

    def get(self, request, format=None):

        all_exp = Expense.objects.all()
        serializer = exp_serializer.ExpenseSerializer(all_exp, many=True)
        return Response(serializer.data, status=ok_restponse)
    
    