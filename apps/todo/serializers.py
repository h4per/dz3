from rest_framework import serializers
from apps.todo.models import ToDo

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo 
        fields = ('title', 'description', 'is_completed', 'created_at', 'image')


class ToDoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('title', 'description', 'is_completed', 'created_at', 'image')
    