from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import tbl_Employees
from .serializers import *

@api_view(['POST'])
def create_employee(request):
    if request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)  # Using request.data, not a string
        if serializer.is_valid():
            serializer.save()  # Save the data to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return the saved employee data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
