from django.contrib import admin
from .models import ICEVehicle, EVVehicle, HEVVehicle

@admin.register(ICEVehicle)
class ICEVehicleAdmin(admin.ModelAdmin):
    list_display = ('name', 'fuel_type', 'price', 'fuel_consumption')
    search_fields = ('name',)

@admin.register(EVVehicle)
class EVVehicleAdmin(admin.ModelAdmin):
    list_display = ('name', 'battery_capacity', 'energy_consumption')
    list_filter = ('battery_capacity',)

@admin.register(HEVVehicle)
class HEVVehicleAdmin(admin.ModelAdmin):
    list_display = ('name', 'fuel_consumption', 'energy_consumption')
