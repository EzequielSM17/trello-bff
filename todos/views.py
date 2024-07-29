from rest_framework import viewsets
from todos.models import ToDo, ToDoTypes, ToDoState
from rest_framework.permissions import AllowAny
from todos.serializers import ToDoSerializer, ToDoTypesSerializer, ToDoStateSerializer
# Create your views here.


class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    permission_classes = [AllowAny]
    serializer_class = ToDoSerializer

    def get_queryset(self):
        return self.queryset.filter(people=self.request.user)


class ToDoTypesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ToDoTypes.objects.all()
    permission_classes = [AllowAny]
    serializer_class = ToDoTypesSerializer


class ToDoStateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ToDoState.objects.all()
    permission_classes = [AllowAny]
    serializer_class = ToDoStateSerializer
