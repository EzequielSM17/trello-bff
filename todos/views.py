from rest_framework import viewsets
from rest_framework import status
from todos.models import ToDo, ToDoTypes, ToDoState
from rest_framework.permissions import IsAuthenticated, AllowAny
from todos.serializers import ToDoSerializer, ToDoTypesSerializer, ToDoStateSerializer, ToDoWithTypeSerializer
from rest_framework.response import Response
# Create your views here.


class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ToDoSerializer

    def get_queryset(self):
        return self.queryset.filter(people=self.request.user)

    def create(self, request):
        try:
            user = self.request.user
            data = {'people': [user.id]}
            data.update(request.data)
            todo_serializer = self.serializer_class(data=data)
            if todo_serializer.is_valid():
                todo_serializer.save()
                return Response({'company': todo_serializer.data}, status=status.HTTP_201_CREATED)
            return Response(todo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": "Error al crear una tarea", "details": str(e)},
                            status=status.HTTP_400_BAD_REQUEST)


class ToDoSpecificStateView(viewsets.ViewSet):
    queryset = ToDo.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ToDoWithTypeSerializer

    def get_queryset(self):
        return self.queryset.filter(people=self.request.user)

    def retrieve(self, request, pk=None):
        queryset = ToDo.objects.all()
        todos = queryset.filter(
            state=pk, people=self.request.user)
        serializer = ToDoWithTypeSerializer(todos, many=True)
        return Response(serializer.data)


class ToDoTypesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ToDoTypes.objects.all()
    permission_classes = [AllowAny]
    serializer_class = ToDoTypesSerializer


class ToDoStateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ToDoState.objects.all()
    permission_classes = [AllowAny]
    serializer_class = ToDoStateSerializer
