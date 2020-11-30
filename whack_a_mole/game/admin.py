from django.contrib import admin

# Register your models here.
from game.models import Result


class PostAdmin(admin.ModelAdmin):
    list_display = ['age', 'score']


admin.site.register(Result, PostAdmin)
