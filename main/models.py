from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#The actual to do lists
class ToDoList(models.Model): #basically creating a database object with each of its attributes/fields defined below
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
    #user is making a link between the logged in user and the list created with a foreignkey.
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

#items for each to do list
class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tdl_items", null=True)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text
