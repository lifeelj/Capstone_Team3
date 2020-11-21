from django.contrib import admin

# Register your models here.

from fitts.models import Tasks

class PostAdmin(admin.ModelAdmin):
    list_display = ['age', 'email', 'transform', 'distance', 'time' ]

admin.site.register(Tasks, PostAdmin)