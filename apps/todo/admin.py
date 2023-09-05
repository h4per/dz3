from django.contrib import admin
from apps.todo.models import ToDo

# Register your models here.
@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'description', 'is_completed', 'created_at', 'image')