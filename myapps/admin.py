from django.contrib import admin

from . import models

@admin.register(models.Plato)
class PlatoModelAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre')

@admin.register(models.Ingrediente)
class IngredienteModelAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'is_vegan', 'is_gluten_free', 'is_kosher')
