from django.contrib import admin
from . models import Reservation

# Register your models here.

@admin.register(Reservation)
class AdminReservation(admin.ModelAdmin):
    list_display = ('name', 'phone', 'number')
    list_filter = ('number', 'date')
    search_fields = ('name', 'phone', 'email',)


