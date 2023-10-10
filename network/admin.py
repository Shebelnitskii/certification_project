from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from network.models import NetworkNode, Contact, Product


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'country', 'city', 'street', 'house_number')


admin.site.register(Contact, ContactAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date', 'manufacturer')


admin.site.register(Product, ProductAdmin)


class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'product_count', 'supplier_link', 'debt', 'get_level')
    list_filter = ('contact__city',)
    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        """ Действие очещения задолженности у выбранных поставщиков """
        queryset.update(debt=0)

    clear_debt.short_description = 'Clear Debt for Selected Nodes'

    def supplier_link(self, obj):
        """ Возвращение ссылки на поставщика"""
        if obj.supplier:
            url = reverse('admin:network_networknode_change', args=[obj.supplier.id])
            return format_html('<a href="{}">{}</a>', url, obj.supplier.name)
        else:
            return '-'

    supplier_link.short_description = 'Поставщик'


admin.site.register(NetworkNode, NetworkNodeAdmin)
