
from expenseApp.models import Expense
from rest_framework import serializers
from django.contrib.auth.models import User

class ExpenseSerializer(serializers.Serializer):
    exp_date    = serializers.DateField(required=True, error_messages={'required': "Expense date is required"})
    exp_title   = serializers.CharField(required=True, error_messages={'required': 'Expense title is required'})
    exp_description = serializers.CharField(style={
        'base_template': "textarea.html"
    }, required=True, error_messages={'required': 'Expense description is required. Explain what, when, where expense happed'})
    exp_user        = serializers.CharField(required=True, error_messages={'required': 'Expense user is required'})

    