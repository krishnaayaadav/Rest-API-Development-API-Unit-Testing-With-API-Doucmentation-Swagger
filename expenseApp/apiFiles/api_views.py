from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from expenseApp.models import Expense
from expenseApp.apiFiles import serializers as exp_serializer
from expenseApp.apiFiles.serializers import ExpenseSerializer
from .paginations import ExpensePagination

from rest_framework.generics import ListAPIView

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse, extend_schema_serializer, extend_schema_field, extend_schema_view, OpenApiExample

# response status codes
ok_restponse = status.HTTP_200_OK
created      = status.HTTP_201_CREATED
not_found    = status.HTTP_404_NOT_FOUND
bad_request  = status.HTTP_400_BAD_REQUEST


ExpenseSerializer = exp_serializer.ExpenseSerializer

# Expense list api 
class ExpenseListAPIView(ListAPIView):

    pagination_class = ExpensePagination  # pagination class
    queryset = Expense.objects.all()      # model querysets
    serializer_class = ExpenseSerializer  # serializer class





# expense api for get and post request without any parameters
class ExpenseAPIView(APIView):
    @extend_schema(
            summary='Get All Expenses',
            description="This endpoint will return all the expense items from database",
            responses = {200: OpenApiResponse(
                            response=exp_serializer.ExpenseSerializer,
                            examples=[
                                        OpenApiExample(
                                        'Valid Response 1',
                                        value={ 'all_expenses':
                                                [
                                                        {
                                                            'pk': 1,
                                                            "exp_user": "krishna",
                                                            "exp_date": "2021-02-12",
                                                            "exp_amount": 4100,
                                                            "exp_title": "Car Services Repair",
                                                            "exp_description": """Sample of descrition: An automobile repair shop (also known regionally as a garage or a workshop) is an establishment """

                                                        },
                                                        {
                                                            'pk': 2,
                                                            "exp_user": "admin",
                                                            "exp_date": "2021-02-12",
                                                            "exp_amount": 2100,
                                                            "exp_title": "Mobile Services Repair",
                                                            "exp_description": """Sample of descrition: An automobile repair shop (also known regionally as a garage or a workshop) is an establishment """

                                                        },

                                                        {
                                                            'pk': 3,
                                                            "exp_user": "krish",
                                                            "exp_date": "2023-02-12",
                                                            "exp_amount": 4004,
                                                            "exp_title": "LPU Collage Fees",
                                                            "exp_description": """Sample of descrition: An automobile repair shop (also known regionally as a garage or a workshop) is an establishment """

                                                        }

                                                ]
                                            
                                            }
                                    ),
                                    ])
                        }
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
        summary='Add new expense item',
        description='This endpoints are use add new expense item in our database using',
        responses={201: OpenApiResponse(response=ExpenseSerializer,
                        examples=[
                            OpenApiExample(
                                'Valid Response 1',
                                value=  { 'data': 
                                            [
                                                {'msg': "Congrats! expense successfully inserted",
                                                    'data': 
                                                    {
                                                        'pk': 1,
                                                        "exp_user": "krishna",
                                                        "exp_date": "2021-02-12",
                                                        "exp_amount": 4100,
                                                        "exp_title": "Car Services Repair",
                                                        "exp_description": """Sample of descrition: An automobile repair shop (also known regionally as a garage or a workshop) is an establishment """

                                                    }
                                                }
                                            ]  
                                        }
                            )
                        ])}
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
    @extend_schema(request=None, summary='Get single expense item',
                    description='Get detail of expense items here',
                    responses={200: OpenApiResponse(response=ExpenseSerializer, 
                                                    examples=[
                                                          OpenApiExample(
                                'Valid Response 1',
                                value=  { 'data': 
                                            [
                                                {'msg': "Detail of expense of id: 1",
                                                    'data': 
                                                    {
                                                        'pk': 1,
                                                        "exp_user": "krishna",
                                                        "exp_date": "2021-02-12",
                                                        "exp_amount": 4100,
                                                        "exp_title": "Car Services Repair",
                                                        "exp_description": """Sample of descrition: An automobile repair shop (also known regionally as a garage or a workshop) is an establishment """

                                                    }
                                                }
                                            ]  
                                        }
                            )
                                                    ]
                                                    )})
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
    @extend_schema(request=None, summary='Update expense partially',
                    description='Update expense data partially',
                    responses={200: OpenApiResponse(response=ExpenseSerializer, 
                                                    examples=[
                                                          OpenApiExample(
                                'Valid Response 1',
                                value=  { 'data': 
                                            [
                                                {'msg': "Congrats expense successfully updated",
                                                    'data': 
                                                    {
                                                        'pk': 1,
                                                        "exp_user": "krishna",
                                                        "exp_date": "2021-02-12",
                                                        "exp_amount": 4100,
                                                        "exp_title": "Car Services Repair",
                                                        "exp_description": """Sample of descrition: An automobile repair shop (also known regionally as a garage or a workshop) is an establishment """

                                                    }
                                                }
                                            ]  
                                        }
                            )
                                                    ]
                                                    )})
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
    @extend_schema(request=None, summary='Update expense completely',
                    description='Update all fields of expense items',
                    responses={200: OpenApiResponse(response=ExpenseSerializer, 
                                                    examples=[
                                                          OpenApiExample(
                                'Valid Response Data',
                                value=  { 'data': 
                                            [
                                                {'msg': "Congrats expense successfully updated",
                                                    'data': 
                                                    {
                                                        'pk': 1,
                                                        "exp_user": "krishna",
                                                        "exp_date": "2021-02-12",
                                                        "exp_amount": 4100,
                                                        "exp_title": "Car Services Repair",
                                                        "exp_description": """Sample of descrition: An automobile repair shop (also known regionally as a garage or a workshop) is an establishment """

                                                    }
                                                }
                                            ]  
                                        }
                            )
                                                    ]
                                                    )})
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
    @extend_schema(summary='Delete expense item',
                   description='Delete particular expense item',
                   responses={
                       204: OpenApiResponse(
                        examples=[OpenApiExample(
                        'Valid Response',
                        value={'msg': "Congrats expense successfully deleted"}
                        )])
                   }
                   )
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
         