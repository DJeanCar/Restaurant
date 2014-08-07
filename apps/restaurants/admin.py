from django.contrib import admin
from .models import Category,City, Comments, Restaurant, Establishment

admin.site.register(Category)
admin.site.register(City)
admin.site.register(Comments)
admin.site.register(Restaurant)
admin.site.register(Establishment)