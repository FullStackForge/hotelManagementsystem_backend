from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.EventType)
admin.site.register(models.EventBooking)
admin.site.register(models.Payment)