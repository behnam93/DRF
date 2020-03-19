from rest_framework import serializers
from app import models


class CalcSerializer(serializers.Serializer):
    num1 = serializers.IntegerField(required=True)
    num2 = serializers.IntegerField(required=True)
    opr = serializers.CharField(required=True, max_length=3)
