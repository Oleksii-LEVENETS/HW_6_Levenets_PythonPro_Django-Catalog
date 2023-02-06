from catalog.models import City, Client, Product, Supplier

from django.contrib import admin


# Register your models here.
admin.site.register(Supplier)
admin.site.register(Product)


class ClientInLine(admin.TabularInline):
    model = Client
    extra = 2


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'state', )
    fieldsets = [
        ("Name of the City", {"fields": ["name"], }),
        ("State of the City", {"fields": ["state"], }),
    ]
    inlines = [ClientInLine]
    list_filter = ['state']
    search_fields = ('name', 'state',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    filter_horizontal = ('products',)
    # raw_id_fields = ("products",)
