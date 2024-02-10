from django.contrib import admin
from stock_options.models import StockItem, Stock

class StockItemAdmin(admin.TabularInline):
    model = StockItem
    list_display = ('ticket', 'price', "kind")

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'price', 'average_price')
    inlines = [StockItemAdmin]