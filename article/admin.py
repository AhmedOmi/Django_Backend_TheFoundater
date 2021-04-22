from django.contrib import admin
from .models import Post


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'updated_on', 'content', 'created_on', 'status')


# Register your models here.

admin.site.register(Post, PostAdmin)
