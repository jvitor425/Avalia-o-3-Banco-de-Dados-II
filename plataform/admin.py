from django.contrib import admin

from .models import VisitDay, Visit, Image, Immobile, Time, City

@admin.register(Immobile)
class ImmobileAdmin(admin.ModelAdmin):
    list_display = ['street', 'value', 'bedrooms', 'size', 'city', 'type_operation', 'type_immobile']
    list_editable = ['type_operation', 'value']
    list_filter = ['type_operation', 'city']


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ['user', 'day', 'time', 'status', 'immobile']
    list_filter = ['day', 'immobile', 'status']


admin.site.register(Image)
admin.site.register(VisitDay)
admin.site.register(Time)