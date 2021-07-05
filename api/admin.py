from django.contrib import admin
from api.models import Catalog, Element


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ("fullname", "version", "start_date")


@admin.register(Element)
class ElementAdmin(admin.ModelAdmin):
    list_display = ("catalog", "element_code")
