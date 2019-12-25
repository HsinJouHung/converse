from django.contrib import admin
from .models import Store,Customer,Product,Company,Warehouse,Inventory,Storage,Purchase
# Register your models here.


admin.site.register(Store)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Inventory)
admin.site.register(Company)
admin.site.register(Warehouse)
admin.site.register(Storage)
admin.site.register(Purchase)