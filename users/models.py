from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

#TODO: groups yapısını kaldırmalısın
#TODO: permission gereksiz


# class User(AbstractUser):
#     ROLES = (
#         ('ADMIN', 'Admin'),
#         ('BLOGGER', 'Blogger'),
#     )
#     role = models.CharField(max_length=10, choices=ROLES)

#     groups = models.ManyToManyField(Group, related_name='custom_user_set')
#     user_permissions = models.ManyToManyField(
#         Permission, related_name='custom_user_set')



class User(AbstractUser):
    ROLES = (
        ('ADMIN', 'Admin'),
        ('BLOGGER', 'Blogger'),
    )
    role = models.CharField(max_length=10, choices=ROLES)

