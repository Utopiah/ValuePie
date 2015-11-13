from django.contrib import admin

# Register your models here.
from .models import Shop
from .models import Client
from .models import Sales
from .models import Valuable
from .models import ValuablePriceSegment
from .models import ValuedPurchase
from .models import Stock

admin.site.register(Shop)
admin.site.register(Client)
admin.site.register(Sales)
admin.site.register(Valuable)
admin.site.register(ValuablePriceSegment)
admin.site.register(ValuedPurchase)
admin.site.register(Stock)
