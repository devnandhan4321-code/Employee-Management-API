from rest_framework.permissions import BasePermission

class EmployeePermission(BasePermission):  
    def has_permission(self,request,view):
        if request.method=='GET':
            return True
        else:
            return request.user.is_authenticated 
    
    
    def has_object_permissions(self,request,view,object): 
        if request.method=="GET":
            return True
        else:
          return request.user.is_superuser 