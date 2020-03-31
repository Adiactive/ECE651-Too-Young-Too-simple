from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        """A string representation of the model."""
        return self.title


class Customer(models.Model):
    first_name = models.CharField("First name", max_length=255)
    last_name = models.CharField("Last name", max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.first_name


class Housing(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    rent = models.FloatField(blank=False, null=False)
    address = models.TextField(blank=True, null=False)
    image = models.ImageField(upload_to='housing_images', default='')

    def __str__(self):
        return "(" + self.owner.username + ")" + self.address
