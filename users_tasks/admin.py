from django.contrib import admin

from .models import (
    Task,
    Priority,
)
# from django_google_maps import widgets as map_widgets
# from django_google_maps import fields as map_fields

admin.site.register(Task)
admin.site.register(Priority)


# class GoogleMapsModelAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         map_fields.AddressField: {
#             'widget': map_widgets.GoogleMapsAddressWidget
#         },
#     }
