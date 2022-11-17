from django.contrib import admin
from .models import Tenant, Unit, Payment
# Register your models here.
admin.site.register(Tenant)
admin.site.register(Unit)
admin.site.register(Payment) 