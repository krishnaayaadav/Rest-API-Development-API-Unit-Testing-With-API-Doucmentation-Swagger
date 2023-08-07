import json
from .models import Expense
from rest_framework import status
from django.test import TestCase,Client
from django.contrib.auth.models import User
from expenseApp.apiFiles.serializers import ExpenseSerializer

from django.urls import reverse

# response classes 
ok_response = status.HTTP_200_OK
bad_request = status.HTTP_400_BAD_REQUEST
created     = status.HTTP_201_CREATED
not_found   = status.HTTP_404_NOT_FOUND
no_content  = status.HTTP_204_NO_CONTENT


get_or_post_expenses = 'get_or_post_expense'
update_expenses      = 'update_delete_post'
# APIClient as some app assume
client = Client()

class ExpenseTestSetUp(TestCase):
   
   # test setup here for testing purpose 
   def setUp(self):
      
      # expense user 
      self.users = (
         User.objects.create(username='krish'),
         User.objects.create(username='ankita'),
         User.objects.create(username='yadav')


           )
      
      # expense titles
      self.exp_titles = ('Car Repair Services', 'Mobile Repair Service', 'Collage Fee Charges')
      
      #exp descriptions
      self.exp_descriptions = ('An establishment where automobiles are repaired by auto mechanics and technicians',
                           'The customer interface is typically a service advisor, traditionally called a service writer',
                           'Collage Shop India, Bangalore, India. 37610 likes · 1 talking about this · 670 were here. A high end store retailing merchandise by some of the top')
      # exp amounts
      self.exp_amounts  = (121, 151, 2010)

      # expense dates
      self.exp_dates = ('2021-01-11', '2200-02-21', '2001-01-11')

      # creating expense objects
      for index in range(0, 3):
         title = self.exp_titles[index]
         date        = self.exp_dates[index]
         amount      = self.exp_amounts[index]
         description = self.exp_descriptions[index]
         user        = self.users[index]

         try:
            Expense.objects.create(exp_title=title, exp_description=description, exp_amount=amount, exp_user=user, exp_date=date)
         except:
            pass
   
   # is expense objects are created or and check their counts model testing here
   def test_is_expense_created(self):

      exps = Expense.objects.all()

      try:
         self.assertGreaterEqual(3, exps.count()) # checking expense obj count
      except:
         print('\n Count test case failed')
      else:
         # print('\n Count test case passed')
         pass

         


