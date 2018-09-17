from rest_framework import viewsets
from api.serializers import CategorySerializer
from api.models import Category


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
