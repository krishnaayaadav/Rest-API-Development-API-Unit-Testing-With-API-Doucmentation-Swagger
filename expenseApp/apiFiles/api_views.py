from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from expenseApp.models import Expense
from expenseApp.apiFiles import serializers as exp_serializer


ok_restponse = status.HTTP_200_OK
created      = status.HTTP_201_CREATED
not_found    = status.HTTP_404_NOT_FOUND
bad_request  = status.HTTP_400_BAD_REQUEST

# expense api for get and post request without any parameters


from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse, extend_schema_serializer, extend_schema_field, extend_schema_view, OpenApiExample
from drf_spectacular.types import OpenApiTypes

class ExpenseAPIView(APIView):
    @extend_schema(
            request=exp_serializer.ExpenseSerializer,
            summary='Get All Expense Items',
            description="This endpoint will return all the expense items from database",
            responses={200: exp_serializer.ExpenseSerializer}
    )
    def get(self, request, format=None):
        all_exp = Expense.objects.all()
        serializer = exp_serializer.ExpenseSerializer(all_exp, many=True)
        response = {
            'msg': "All expense data",
            'data': serializer.data,
        }
        return Response(response, status=ok_restponse)
    
    # add/post/insert new expense into db
    @extend_schema(
            request=exp_serializer.ExpenseSerializer,
            responses={201: exp_serializer.ExpenseSerializer}
    )
    def post(self, request, format=None):
                                   # request.data contains parsed data of user request
        serializer  = exp_serializer.ExpenseSerializer(data=request.data)
        if serializer.is_valid():  # checking serializer validation here
            serializer.save()      # saving data into db
            response = {
                'msg': 'Congrats! expense successfully inserted',
                'data': serializer.data
            }
            return Response(response, status=created)
        else:
            return Response(serializer.errors, status=bad_request)

# expense api for updation, deletion, single item 
class ExpenseUpdateAPI(APIView):
    
    # GET request to fetch single/details of particular expense item
    def get(self, request, expId, format=None):
        error_response = {
            'data': f"Expense does found with this {expId}",
            'status': not_found
        }
        try:
            expense = Expense.objects.get(pk=expId)

        except Expense.DoesNotExist:
            return Response(error_response, status=not_found)  # expense does not exist error

        except Expense.MultipleObjectsReturned:
            return Response(error_response, status=not_found)  # multiple expense found errro


        else: # if expense found
            serializer = exp_serializer.ExpenseSerializer(expense)
            response = {
                'msg': f"Detail of expense of id: {expId}",
                "data": serializer.data
            }
            return Response(response, status=ok_restponse)
    
    # PARCH  request for partial updation
    def patch(self, request, expId, format=None):
        error_response = {
            'data': f"Expense does found with this {expId}",
            'status': not_found
        }
        try:
            expense = Expense.objects.get(pk=expId)

        except Expense.DoesNotExist:
            return Response(error_response, status=not_found)  # expense does not exist error

        except Expense.MultipleObjectsReturned:
            return Response(error_response, status=not_found)  # multiple expense found errro

        else: # if expense found
            serializer = exp_serializer.ExpenseSerializer(expense, data=request.data, partial=True, context={'expense': expense})

            # checking serializer validation here
            if serializer.is_valid():
                serializer.save() # then store serialized data into db
                response = {
                    'msg': 'Congrats expense successfully updated',
                    'data': serializer.data
                }
                return Response(response, ok_restponse)
            else:
                return Response(serializer.errors, status=bad_request)
    
    # PUT request for complete updation here
    def put(self, request, expId, format=None):
        error_response = {
            'data': f"Expense does found with this {expId}",
            'status': not_found
        }
        try:
            expense = Expense.objects.get(pk=expId)

        except Expense.DoesNotExist:
            return Response(error_response, status=not_found)  # expense does not exist error

        except Expense.MultipleObjectsReturned:
            return Response(error_response, status=not_found)  # multiple expense found errro


        else: # if expense found
            serializer = exp_serializer.ExpenseSerializer(expense, data=request.data)

            # checking serializer validation here
            if serializer.is_valid():
                serializer.save() # then store serialized data into db
                response = {
                    'msg': 'Congrats expense successfully updated',
                    'data': serializer.data
                }
                return Response(response, ok_restponse)
            else:
                return Response(serializer.errors, status=bad_request)
    
    # delete some existing expense item here
    def delete(self, request, expId, format=None):
        error_response = {
            'data': f"Expense does found with this {expId}",
            'status': not_found
        }
        try:
            expense = Expense.objects.get(pk=expId)

        except Expense.DoesNotExist:
            return Response(error_response, status=not_found)  # expense does not exist error

        except Expense.MultipleObjectsReturned:
            return Response(error_response, status=not_found)  # multiple expense found errro

        else: # if expense found then

            try:
                expense.delete() # deleting here expense obj
            except:
                return Response({'error': 'Error while performing deletion'}, status=status.HTTP_409_CONFLICT)
            else:
                response = {
                    'msg': 'Congrats expense successfully deleted',
                }
                return Response(response, status=status.HTTP_204_NO_CONTENT)
            