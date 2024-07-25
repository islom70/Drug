from django.core.validators import FileExtensionValidator
from django.db import models


class Drug(models.Model):
    title = models.CharField(max_length=150)
    summary = models.CharField(max_length=255)
    body = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='drugs/images/', blank=True, null=True, validators=[
        FileExtensionValidator(allowed_extensions=['jpg', 'svg', 'png', 'jpeg'])
    ])

    def __str__(self):
        return self.title

    objects = models.Manager()


class Contact(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.name

    objects = models.Manager()


class Order(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    drug_type = models.ForeignKey(Drug, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.name

    objects = models.Manager()
