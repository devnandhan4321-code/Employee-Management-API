from django.contrib import admin
from employee.models import Employee
# Register your models here.


admin.site.register(Employee)

def ready(self):
    import employee.signals