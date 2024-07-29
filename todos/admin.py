from django.contrib import admin

from todos.models import ToDo, ToDoTypes, ToDoState

# Register your models here.

admin.site.register(ToDo)
admin.site.register(ToDoTypes)
admin.site.register(ToDoState)
