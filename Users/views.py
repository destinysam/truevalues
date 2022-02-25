from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets,filters,status
from .serializers import UserSerializer
from .models import UserModel
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
# Create your views here.
class UserView(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name']
    def get_queryset(self):
        field = self.request.query_params.get("sort")
        if field is None:
            queryset = UserModel.objects.all()
        else:
            queryset = UserModel.objects.all().order_by(field)
        return queryset
    