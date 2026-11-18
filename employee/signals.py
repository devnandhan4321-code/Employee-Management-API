from django.db.models.signals import pre_save
from django.dispatch import receiver

from employee.models import Employee


@receiver(pre_save, sender=Employee)
def uppercase_name(sender, instance, **kwargs):

    instance.name = instance.name.upper()