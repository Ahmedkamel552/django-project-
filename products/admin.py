from django.contrib import admin
from .models import product, Offer


class productAdmin(admin.ModelAdmin):
    list_display = ("name", "stock", "price")


class OfferAdmin(admin.ModelAdmin):
    list_display = ("code", "discount")


admin.site.register(Offer, OfferAdmin)
admin.site.register(product, productAdmin)
