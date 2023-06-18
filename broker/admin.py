from django.contrib import admin
from broker.models import Broker, Options

class OptionsAdmin(admin.TabularInline):
    model = Options
    list_display = ('broker', 'flat_tax', 'fromm', 'to',  'size', )
    verbose_name = 'option'
    verbose_name_plural = 'options'

@admin.register(Broker)
class BrokerAdmin(admin.ModelAdmin):
    list_display = ('name', )
    inlines = [OptionsAdmin,]