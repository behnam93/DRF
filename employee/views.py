from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmployeeSerializer
from .models import Employee


@api_view(['POST'])
def post_employee(request):
    data = {
        'name': request.data['name'],
        'age': request.data['age'],
        'salary': request.data['salary'],
        'post': request.data['post']
    }
    ser = EmployeeSerializer(data=data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data, status=status.HTTP_201_CREATED)
    else:
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
