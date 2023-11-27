from django.contrib import admin
from .models import Order, OrderLineItem
from django.db.models import Sum


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = ('order_number', 'date', 'order_total', 'grand_total',)
    fields = ('order_number', 'date', 'full_name', 'email', 'order_total', 'grand_total', 'user_profile')
    list_display = ('order_number', 'date', 'full_name', 'order_total', 'grand_total', 'total_brushes_sold', 'total_sales')
    ordering = ('-date',)

    def total_brushes_sold(self, obj):
        return OrderLineItem.objects.count()
    total_brushes_sold.short_description = 'Total Brushes Sold'

    def total_sales(self, obj):
        total = Order.objects.aggregate(total=Sum('grand_total'))['total']
        return f"${total:.2f}" if total else "$0.00"
    total_sales.short_description = 'Total Sales'


admin.site.register(Order, OrderAdmin)
