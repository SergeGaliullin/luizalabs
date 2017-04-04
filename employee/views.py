from rest_framework import mixins
from rest_framework import generics
from .models import Employee


class EmployeeList(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Employee.object.all()
    serializer_class = EmployeeSerializer
    
