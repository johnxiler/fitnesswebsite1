from django.db import models
# from django.contrib.auth.models import AbstractUser, Group

# Create your models here.


# class Coach(models.Model):
#     # Additional fields for the regular user in the fitness industry
#     height = models.FloatField()
#     weight = models.FloatField()
#     age = models.IntegerField()
#     fitness_goal = models.CharField(max_length=100)

# def is_staff(self):
#     return True


# class Trainee(models.Model):
#     # Additional fields for the regular user in the fitness industry
#     height = models.FloatField()
#     weight = models.FloatField()
#     age = models.IntegerField()
#     fitness_goal = models.CharField(max_length=100)
# image = models.FileField(upload_to=UploadToPathAndRename(settings.TEACHERS_IMAGES_DIR), blank=True, null=True, verbose_name=_('Teacher logo'))
#     name = models.CharField(blank=False, null=False, default=None, max_length=255, validators=[MaxLengthValidator(255)], verbose_name=_('Name'))
#     street = models.CharField( max_length=128, blank=False, null=True, default=None, verbose_name=_('Street'))
#     created_by = models.ForeignKey('Profiles', null=True, blank=True, on_delete=models.SET_NULL)
