from django.contrib import admin

from .models import GPUModel, HistoricalPrice

admin.site.register(GPUModel, HistoricalPrice)
