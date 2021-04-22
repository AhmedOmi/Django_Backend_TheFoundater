from django.db import models


# Create your models here.
class Newsletter(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=254)
