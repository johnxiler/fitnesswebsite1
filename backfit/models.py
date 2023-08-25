# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from frontfit.models import Coach
# Create your models here.


# class Profiles(AbstractUser):
#     date_of_birth = models.DateField(max_length=128,
#                                      blank=True, null=True,
#                                      default=None,
#                                      verbose_name=(u'Date of birth'))
#     Coach = models.OneToOneField(Coach, null=True, blank=True,
#                                  verbose_name=(u'Coach'),
#                                  on_delete=models.CASCADE)
    # Admin = models.OneToOneField(Admin, null=True, blank=True,
    #                              verbose_name=(u'Admin'),
    #                              on_delete=models.CASCADE)

    # class Meta:
    #     db_table = 'profiles'
    #     verbose_name = ('Profile')
    #     verbose_name_plural = ('Profiles')


# class Admin(AbstractUser):
#     # Add any additional fields specific to the admin user
#     department = models.CharField(max_length=100)
#     can_manage_users = models.BooleanField(default=False)

#     def is_staff(self):
#         return True

#     def has_user_management_privilege(self):
#         return self.can_manage_users
