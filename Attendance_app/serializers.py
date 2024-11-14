from .models import *
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = tbl_Employees
        fields = '__all__'