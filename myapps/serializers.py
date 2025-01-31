from rest_framework import serializers
from . import models

class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ingrediente
        fields = (
            'id', 'nombre', 'is_vegan', 'is_gluten_free', 'is_kosher'
        )

class PlatoSerializer(serializers.ModelSerializer):
    ingredientes = serializers.PrimaryKeyRelatedField(queryset=models.Ingrediente.objects.all(), many=True)
    is_vegan = serializers.ReadOnlyField()
    is_gluten_free = serializers.ReadOnlyField()
    is_kosher = serializers.ReadOnlyField()
    
    class Meta:
        fields = (
            'id', 'nombre', 'ingredientes', 'is_vegan', 'is_gluten_free', 'is_kosher'
        )
        model = models.Plato

class PlatoDetailSerializer(PlatoSerializer):
    ingredientes = IngredienteSerializer(many=True, read_only=True)