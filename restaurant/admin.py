from django.contrib import admin
from django.utils.html import format_html
from .models import Menu, Booking

class MenuAdmin(admin.ModelAdmin):
    readonly_fields = ('image_preview',)  # Only show image preview in form

    def image_preview(self, obj):
        """Display a small preview of the uploaded image."""
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" style="border-radius:5px;"/>', obj.image.url)
        return "No Image"

    image_preview.short_description = "Image Preview"

# Register your models here.
admin.site.register(Menu, MenuAdmin)
admin.site.register(Booking)
