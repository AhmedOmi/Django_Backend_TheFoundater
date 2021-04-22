from django.contrib import admin
from .models import Newsletter


# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'email')


# Register your models here.

admin.site.register(Newsletter, NewsAdmin)
