from django.contrib import admin

from .models import Drug, Contact, Order

admin.site.register(Drug)
admin.site.register(Contact)
admin.site.register(Order)
