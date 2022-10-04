from django.contrib import admin

# Register your models here.

from .models import Post, Topic, Message, AppUser

admin.site.register(AppUser)
admin.site.register(Post)
admin.site.register(Topic)
admin.site.register(Message)