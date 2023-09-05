from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from apps.todo.models import ToDo 
from apps.todo.serializers import ToDoSerializer, ToDoDetailSerializer
from apps.todo.permissions import ToDoPermission

# Create your views here.
class ToDoAPIViewSet(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['user', 'title', 'description']
    search_fields = ['user__username', 'title', 'description']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ToDoDetailSerializer
        return ToDoSerializer
    
    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (ToDoPermission(), )
        return (AllowAny(), )
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)