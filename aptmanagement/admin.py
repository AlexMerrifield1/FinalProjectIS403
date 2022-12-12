from django.contrib import admin

# Register your models here.
from .models import Tennant, Admin


admin.site.register(Tennant)
admin.site.register(Admin)