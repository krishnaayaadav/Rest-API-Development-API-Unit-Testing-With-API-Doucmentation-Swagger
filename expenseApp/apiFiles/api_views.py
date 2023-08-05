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
    # get all expense here
    def get(self, request, format=None):

        all_exp = Expense.objects.all()
        serializer = exp_serializer.ExpenseSerializer(all_exp, many=True)
        return Response(serializer.data, status=ok_restponse)
    
    # add/post/insert new expense into db
    def post(self, request, format=None):
                                   # request.data contains parsed data of user request
        serializer  = exp_serializer.ExpenseSerializer(data=request.data)
        if serializer.is_valid():  # checking serializer validation here
            serializer.save()      # saving data into db
            return Response(serializer.data, status=created)
        else:
            return Response(serializer.errors, status=bad_request)

