from django.contrib import admin

# Register your models here.
from core.models import Marca, Categoria

admin.site.register(Marca)
admin.site.register(Categoria)