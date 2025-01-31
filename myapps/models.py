from django.db import models


class Ingrediente(models.Model):
    nombre = models.CharField(verbose_name='Nombre', max_length=100, unique=True)
    is_vegan = models.BooleanField(verbose_name='Is vegan', default=False)
    is_gluten_free = models.BooleanField(verbose_name='Is gluten free', default=False)
    is_kosher = models.BooleanField(verbose_name='Is kosher', default=False)

    def __str__(self):
        return self.nombre

class Plato(models.Model):
    nombre = models.CharField(verbose_name='Nombre', max_length=100, unique=True)
    ingredientes = models.ManyToManyField('Ingrediente', verbose_name='Ingredientes')

    @property
    def is_vegan(self):
        return all(ing.is_vegan for ing in self.ingredientes.all())

    @property
    def is_gluten_free(self):
        return all(ing.is_gluten_free for ing in self.ingredientes.all())

    @property
    def is_kosher(self):
        return all(ing.is_kosher for ing in self.ingredientes.all())

    def __str__(self):
        return self.nombre

