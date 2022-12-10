from .models import Tata
from rest_framework import serializers


class Tataserializer(serializers.Serializer):
    Name=serializers.CharField(max_length= 30)
    Email=serializers.EmailField()
    Price=serializers.IntegerField()
    Model=serializers.DateField()
    Chassis=serializers.CharField(max_length=30)


    def create(self, validated_data):
        print("create method is called ")
        return Tata.objects.create(**validated_data)

    def update(self, employee, validated_data):
        newemp=Tata(**validated_data)
        newemp.id= employee.id
        newemp.save()
        return newemp
    
       

class userserializer(serializers.Serializer):
    username=serializers.CharField( max_length = 30)
    email=serializers.EmailField()
    password=serializers.CharField(max_length = 30)
  
    
