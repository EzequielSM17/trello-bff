from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register('todos', views.ToDoViewSet, basename='todos')
router.register('todo_types', views.ToDoTypesViewSet, basename='todo_types')
router.register('todo_state', views.ToDoStateViewSet, basename='todo_state')

app_name = 'todos'

urlpatterns = [
    path('', include(router.urls))
]
