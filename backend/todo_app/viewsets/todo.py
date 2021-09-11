from todo_app.serializers import TodoSerializer
from todo_app.models import Todo
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

class TodoViewSet (ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get','post','put','delete']
    lookup_field = 'id'



