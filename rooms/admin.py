from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe
# Register your models here.
admin.site.register(models.Room)
admin.site.register(models.Booking)
admin.site.register(models.Payment)
admin.site.register(models.Gallery)

class RoomImageInline(admin.TabularInline):
    model = models.RoomImage
    extra = 1

class RoomTypeAdmin(admin.ModelAdmin):
    inlines = [RoomImageInline]
    list_display = ['title','first_image']
    search_fields = ['title']
    def first_image(self,obj):
        first_image = obj.room_type_imgs.first()
        if first_image:
            return mark_safe('<img src = "%s" width="50"/>' % first_image.image.url)
    first_image.allow_tags = True
admin.site.register(models.RoomType,RoomTypeAdmin)
admin.site.register(models.RoomImage)