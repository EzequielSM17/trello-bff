from rest_framework import serializers
from users.models import User
from todos.models import ToDoTypes, ToDo, ToDoState


class ToDoSerializer(serializers.ModelSerializer):
    people = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=User.objects.all()
    )

    class Meta:
        model = ToDo
        fields = ('id', 'title', 'description',
                  'date', 'deadline', 'people', 'type')
        read_only_Fields = ('id',)


class ToDoTypesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ToDoTypes
        fields = ('id', 'title', 'priority')
        read_only_Fields = ('id',)


class ToDoStateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ToDoState
        fields = ('id', 'name')
        read_only_Fields = ('id',)
