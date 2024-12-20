from django.contrib import admin
# Register your models here.
from . import models
admin.site.register(models.Review)
admin.site.register(models.Contact)
admin.site.register(models.Profile)
admin.site.register(models.Career)
admin.site.register(models.Banners)
admin.site.register(models.ControlPanel)