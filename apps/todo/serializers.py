from rest_framework import serializers
from apps.todo.models import ToDo

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo 
        fields = "__all__"


class ToDoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = "__all__"
