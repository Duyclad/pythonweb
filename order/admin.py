from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'shipping_address', 'order_description',
                    'is_completed']
    list_filter = ['id']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
