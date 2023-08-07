from django.db import models
from django.contrib.auth.models import User

# expense model
class Expense(models.Model):
    exp_date        = models.DateField()
    exp_title       = models.CharField(max_length=250)
    exp_description = models.TextField(blank=True,null=True)
    exp_amount      = models.PositiveIntegerField(default=100)
    exp_user        = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')

    def __str__(self):
        return f'{self.exp_title} | {self.exp_user}'
    
    
