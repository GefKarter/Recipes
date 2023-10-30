from rest_framework import viewsets, permissions
from .models import *
from .serializers import *


class RecipeViewset(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RecipeSerializer