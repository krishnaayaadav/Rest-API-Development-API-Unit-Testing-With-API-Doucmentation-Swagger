
from rest_framework import serializers
from expenseApp.models import Expense
from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
   
# Expense Serializer class
class ExpenseSerializer(serializers.Serializer):
    pk          = serializers.IntegerField(required=False)
    exp_date    = serializers.DateField(required=False, error_messages={'required': "Expense date is required"})
    exp_title   = serializers.CharField(required=False, error_messages={'required': 'Expense title is required'})
    exp_description = serializers.CharField(style={
        'base_template': "textarea.html"
    }, required=False, error_messages={'required': 'Expense description is required. Explain what, when, where expense happed'})
    exp_user        = serializers.CharField(required=False, error_messages={'required': 'Expense user is required'})
    exp_amount      = serializers.IntegerField(error_messages={'required': "Expense amount is required"})

    # custom serializer validation
    def validate(self, attrs):
        exp_date = attrs.get('exp_date', None)
        exp_title= attrs.get('exp_title', None)
        exp_desc = attrs.get('exp_description', None)
        exp_user = attrs.get('exp_user', None)
        exp_amount = attrs.get('exp_amount', None)


        expense = self.context.get('expense', None) # for partial updation

        # all field required validation here
        if not expense:
            if not exp_title:
                raise serializers.ValidationError({'exp_title': "Expense title is requierd"})
            
            if not exp_desc :
                raise serializers.ValidationError({'exp_description': 'Expense is requierd'})
            
            if not exp_user:
                raise serializers.ValidationError({'exp_user': "Expense user is required"})
            
            if not exp_amount:
                raise serializers.ValidationError({'exp_amount': "Expense amount is requierd"})
            
            # expense data is none
            if not exp_date:
                raise serializers.ValidationError({'exp_date': 'Expense data is required'})

        # title validation
        if exp_title:
            if len(exp_title) < 7:
                raise serializers.ValidationError({'exp_title': 'Expense title at least contains 7 characters'})
        
        # description validation
        if exp_desc:
            if len(exp_desc) <11:
                raise serializers.ValidationError({'exp_description': "Expense description atleast contains 11 characters"})

        # checking here valid user
        if exp_user:
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
    
    # update method here
    def update(self, instance, validated_data):
        # instance means old data
        # validated_data: means new which is comming for updation
        
        # updating instance data here
        instance.exp_title = validated_data.get('exp_title', instance.exp_title)
        instance.exp_date  = validated_data.get('exp_date', instance.exp_date)
        instance.exp_user  = validated_data.get('exp_user', instance.exp_user)
        instance.exp_description = validated_data.get('exp_description', instance.exp_description)
        instance.exp_amount = validated_data.get('exp_amount', instance.exp_amount)

        instance.save() # saving data here
        return instance
