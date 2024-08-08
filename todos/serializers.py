from rest_framework import serializers
from users.models import User
from todos.models import ToDoTypes, ToDo, ToDoState


class ToDoTypesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ToDoTypes
        fields = ('id', 'name', 'priority')
        read_only_Fields = ('id',)


class ToDoStateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ToDoState
        fields = ('id', 'name')
        read_only_Fields = ('id',)


class ToDoSerializer(serializers.ModelSerializer):
    people = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=User.objects.all()
    )

    class Meta:
        model = ToDo
        fields = ('id', 'title', 'description',
                  'date', 'deadline', 'people', 'type', 'state')
        read_only_Fields = ('id',)


class ToDoWithTypeSerializer(serializers.ModelSerializer):
    people = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=User.objects.all()
    )
    type = ToDoTypesSerializer()

    class Meta:
        model = ToDo
        fields = ('id', 'title', 'description',
                  'date', 'deadline', 'people', 'type', 'state')
        read_only_Fields = ('id',)
