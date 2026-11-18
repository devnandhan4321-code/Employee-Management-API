from rest_framework import serializers
from employee.models import Employee
from django.contrib.auth.models import User


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=20)
    class Meta:

        model=User
        fields=['username','email','password']


    def create(self,validate_data):
            u=Employee.objects.create_user(**validate_data)
            u.save
            return u