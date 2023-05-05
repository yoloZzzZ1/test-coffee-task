import os

from django.dispatch import receiver
from django.db.models.signals import pre_save
from ..models import FirstSection, SecondSection, ThirdSection

"""
Не стал пушить в селери т.к не так много полей
"""

@receiver(pre_save, sender=FirstSection)
def auto_delete_file_on_change_first_section(sender, instance, **kwargs):
    for field_name in ['first_slide', 'second_slide', 'third_slide', 'fourth_slide']:
        try:
            old_instance = sender.objects.get(pk=instance.pk)
        except sender.DoesNotExist:
            return False
        old_file = getattr(old_instance, field_name)
        new_file = getattr(instance, field_name)
        if not old_file == new_file and bool(old_file):
            if os.path.isfile(old_file.path):
                os.remove(old_file.path)


@receiver(pre_save, sender=SecondSection)
def auto_delete_file_on_change_second_section(sender, instance, **kwargs):
    for field_name in ['first_object_image', 'second_object_image', 'third_object_image']:
        try:
            old_instance = sender.objects.get(pk=instance.pk)
        except sender.DoesNotExist:
            return False
        old_file = getattr(old_instance, field_name)
        new_file = getattr(instance, field_name)
        if not old_file == new_file and bool(old_file):
            if os.path.isfile(old_file.path):
                os.remove(old_file.path)


@receiver(pre_save, sender=ThirdSection)
def auto_delete_file_on_change_third_section(sender, instance, **kwargs):
    for field_name in ['first_slide', 'second_slide', 'third_slide', 'fourth_slide']:
        try:
            old_instance = sender.objects.get(pk=instance.pk)
        except sender.DoesNotExist:
            return False
        old_file = getattr(old_instance, field_name)
        new_file = getattr(instance, field_name)
        if not old_file == new_file and bool(old_file):
            if os.path.isfile(old_file.path):
                os.remove(old_file.path)