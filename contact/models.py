from django.db import models


class Contact(models.Model):
    email = models.EmailField(max_length=254)
    firstName = models.CharField(max_length=254)
    lastName = models.CharField(max_length=254)
    phone = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
