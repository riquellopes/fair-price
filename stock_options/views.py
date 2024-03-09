# from django.shortcuts import render
from django.views.generic import ListView
from stock_options.models import Stock

# Create your views here.
class StockViews(ListView):
    model = Stock