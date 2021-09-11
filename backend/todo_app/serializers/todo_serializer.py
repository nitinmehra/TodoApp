from todo_app.models import Todo
from rest_framework.serializers import ModelSerializer

class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id' ,'title', 'description', 'completed','created_at')
