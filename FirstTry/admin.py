from django.contrib import admin

from .models import Person, Favourite

admin.site.register(Person)
admin.site.register(Favourite)