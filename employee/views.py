from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from employee.models import Employee
from employee.serializer import EmployeeSerializer,RegisterSerializer
from employee.permissions import EmployeePermission
# Create your views here.
class EmployeelistCreate(APIView):
    permission_classes=[EmployeePermission]
   

    def get(self,request):
        e=Employee.objects.all()
        serializer_instance=EmployeeSerializer(e,many=True)
        return Response(serializer_instance.data,status.HTTP_201_CREATED)

    def post(self,request):
        serializer_instance=EmployeeSerializer(data=request.data)
        if serializer_instance.is_valid():
           serializer_instance.save(organizer=request.user)
           return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
           return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
       
class EmployeeRetrieveUpdateDelete(APIView):

    permission_classes = [EmployeePermission]
    def get(self, request, pk):

        p = get_object_or_404(Employee, id=pk)

        self.check_object_permissions(request, p)

        serializer_instance = EmployeeSerializer(p)

        return Response(serializer_instance.data,status=status.HTTP_200_OK)
        

   
    def put(self, request, pk):

        p = get_object_or_404(Employee, id=pk)

        self.check_object_permissions(request, p)

        serializer_instance = EmployeeSerializer(
            instance=p,
            data=request.data
        )

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(
                serializer_instance.data,
                status=status.HTTP_200_OK
            )

        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
            

    
    def delete(self, request, pk):

        p = get_object_or_404(Employee, id=pk)

        self.check_object_permissions(request, p)

        p.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
        
class Register(APIView):
    def post(self,request):
        serializer_instance=RegisterSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)