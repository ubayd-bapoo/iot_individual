from django.contrib import admin
from .models import SensehatReading

class SensehatReadingAdmin(admin.ModelAdmin):
    list_display = ('created', 'sensehat_sensor', 'reading', 'source')
    list_filter = ('source',)


admin.site.register(SensehatReading, SensehatReadingAdmin)

