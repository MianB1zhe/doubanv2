from django.contrib import admin

# Register your models here.

from books import models
admin.site.register(models.DoubanUser)
admin.site.register(models.DoubanBook)
admin.site.register(models.UserReadBooks)