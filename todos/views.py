from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from todos.models import ToDo, ToDoTypes, ToDoState
from rest_framework.permissions import IsAuthenticated, AllowAny
from todos.serializers import ToDoSerializer, ToDoTypesSerializer, ToDoStateSerializer
from rest_framework.response import Response
# Create your views here.


class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ToDoSerializer

    def get_queryset(self):
        return self.queryset.filter(people=self.request.user)


class ToDoSpecificStateView(viewsets.ViewSet):
    queryset = ToDo.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ToDoSerializer

    def get_queryset(self):
        return self.queryset.filter(people=self.request.user)

    def retrieve(self, request, pk=None):
        queryset = ToDo.objects.all()
        todos = queryset.filter(
            state=pk, people=self.request.user)
        serializer = ToDoSerializer(todos, many=True)
        return Response(serializer.data)


class ToDoTypesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ToDoTypes.objects.all()
    permission_classes = [AllowAny]
    serializer_class = ToDoTypesSerializer


class ToDoStateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ToDoState.objects.all()
    permission_classes = [AllowAny]
    serializer_class = ToDoStateSerializer
