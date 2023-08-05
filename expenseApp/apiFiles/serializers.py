
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

    # custom serializer validation
    def validate(self, attrs):
        exp_date = attrs.get('exp_date', None)
        exp_title= attrs.get('exp_title', None)
        exp_desc = attrs.get('exp_description', None)
        exp_user = attrs.get('exp_user', None)
        
        # title validation
        if len(exp_title) < 7:
            raise serializers.ValidationError({'exp_title': 'Expense title at least contains 7 characters'})
        
        # description validation
        if str(len(exp_desc)) <11:
            raise serializers.ValidationError({'exp_description': "Expense description atleast contains 11 characters"})
        
        # checking here valid user
        try:
            user = User.objects.get(username=exp_user)
        except:
            raise serializers.ValidationError({'exp_user': "Expense user is invalid"})
        else:
            attrs['exp_user'] = user # changing via user object here

        return attrs
   
    # Create method
    def create(self, validated_data):
        return Expense.objects.create(**validated_data)
    
