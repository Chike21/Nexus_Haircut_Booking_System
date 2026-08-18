# Register your models here.
from django.contrib import admin # type: ignore
from .models import Appointment, Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'service',
        'date',
        'time',
        'status',
        'user',
    )

    list_filter = (
        'status',
        'service',
        'date',
    )

    search_fields = (
        'name',
        'phone',
        'email',
    )

    ordering = ('date',)

    list_editable = ('status',)