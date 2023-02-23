from django.db import models

class User(models.Model):
    email = models.EmailField(max_length=120, unique=True, null=False)
    password = models.CharField(max_length=120, unique=True, null=False)

    def __str__(self) -> str:
        return f'User with email: {self.email}'


class Shopping_list(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    label = models.CharField(max_length=120)
    price = models.FloatField()

    def __str__(self) -> str:
        return self.label