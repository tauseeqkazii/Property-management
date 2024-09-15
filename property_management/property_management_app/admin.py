from django.contrib import admin
from .models import Property, Tenant, Payment

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'owner', 'number_of_units')

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'rented_property', 'move_in_date', 'rent_due_date')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'amount', 'payment_date', 'status')

