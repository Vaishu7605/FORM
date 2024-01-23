from django.contrib import admin
from .models import *
@admin.register(register)

class clientAdmin(admin.ModelAdmin):
    list_display=('id','first_name','last_name','email','password','confirm_password','contact_number')

# Register your models here.
