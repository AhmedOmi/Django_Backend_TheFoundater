from django.contrib import admin
from .models import Contact


# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'firstName', 'lastName', 'phone', 'message')


# Register your models here.

admin.site.register(Contact, ContactAdmin)
