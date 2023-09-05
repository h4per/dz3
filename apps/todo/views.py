from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.todo.models import ToDo 
from apps.todo.serializers import ToDoSerializer, ToDoDetailSerializer
from apps.users.permissions import UserPermission

# Create your views here.
class ToDoAPIViewSet(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    
    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (UserPermission(), )
        return (AllowAny(), )
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)