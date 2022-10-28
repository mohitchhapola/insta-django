from django.contrib import admin
from innerinsta.models import data
# Register your models here.

class InstaAdmin(admin.ModelAdmin):
    list_display=('username','password')

admin.site.register(data, InstaAdmin)    