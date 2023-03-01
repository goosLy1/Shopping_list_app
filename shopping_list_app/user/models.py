from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# class User(models.Model):
#     email = models.EmailField(max_length=120, unique=True, null=False)
#     password = models.CharField(max_length=120, unique=True, null=False)

#     def __str__(self) -> str:
#         return f'User with email: {self.email}'


class Shopping_list(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    label = models.CharField(max_length=120)
    

    def __str__(self) -> str:
        return self.label