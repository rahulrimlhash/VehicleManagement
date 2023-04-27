from django.contrib import admin
from vehicleApp.models import Vehicle
# Register your models here.
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle_number','vehicle_model')

admin.site.register(Vehicle,VehicleAdmin)

