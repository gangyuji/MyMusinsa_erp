from django.contrib import admin
from erp.models import ProductModel, InBound, OutBound, Inventory
# Register your models here.
admin.site.register(ProductModel)
admin.site.register(InBound)
admin.site.register(OutBound)
admin.site.register(Inventory)