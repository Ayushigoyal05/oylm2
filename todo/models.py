from django.db import models
import datetime

# Create your models here.
class ListTodo(models.Model):
    todo=models.CharField( max_length=250)
    completed=models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.todo)
    


