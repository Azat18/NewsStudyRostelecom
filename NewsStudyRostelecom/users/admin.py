from django.contrib import admin
from .models import *

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'gender']
    list_filter = ['user', 'gender']

admin.site.register(Account,AccountAdmin)
