from rest_framework import status
from rest_framework.test import APITestCase
from .models import Ingrediente, Plato

class IngredienteCRUDTests(APITestCase):
    
    def setUp(self):
        self.nuevo_ingrediente = {
            'nombre': 'Acelga',
            'is_vegan': True,
            'is_gluten_free': True,
            'is_kosher': False
        }

        self.url_api = '/api/v1/ingredientes/'
    
    def test_create_ingrediente(self):
        response = self.client.post(self.url_api, self.nuevo_ingrediente, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['nombre'], self.nuevo_ingrediente['nombre'])
        self.assertEqual(response.data['is_vegan'], self.nuevo_ingrediente['is_vegan'])
        self.assertEqual(response.data['is_gluten_free'], self.nuevo_ingrediente['is_gluten_free'])
        self.assertEqual(response.data['is_kosher'], self.nuevo_ingrediente['is_kosher'])

    def test_read_ingrediente(self):
        response_create = self.client.post(self.url_api, self.nuevo_ingrediente, format='json')
        ingrediente_id = response_create.data['id']

        response = self.client.get(f"{self.url_api}{ingrediente_id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], ingrediente_id)
        self.assertEqual(response.data['nombre'], self.nuevo_ingrediente['nombre'])

    def test_update_ingrediente(self):
        response_create = self.client.post(self.url_api, self.nuevo_ingrediente, format='json')
        ingrediente_id = response_create.data['id']

        ingrediente_actualizado = {
            'nombre': 'Acelga fresca',
            'is_vegan': True,
            'is_gluten_free': True,
            'is_kosher': True
        }
        
        response_update = self.client.put(f"{self.url_api}{ingrediente_id}/", ingrediente_actualizado, format='json')
        self.assertEqual(response_update.status_code, status.HTTP_200_OK)
        self.assertEqual(response_update.data['nombre'], ingrediente_actualizado['nombre'])
        self.assertEqual(response_update.data['is_kosher'], ingrediente_actualizado['is_kosher'])

    def test_delete_ingrediente(self):
        response_create = self.client.post(self.url_api, self.nuevo_ingrediente, format='json')
        ingrediente_id = response_create.data['id']

        response_delete = self.client.delete(f"{self.url_api}{ingrediente_id}/")
        self.assertEqual(response_delete.status_code, status.HTTP_204_NO_CONTENT)
        
        response_get = self.client.get(f"{self.url_api}{ingrediente_id}/")
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)



class PlatoTests(APITestCase):
    
    def setUp(self):
        self.ingrediente1 = Ingrediente.objects.create(
            nombre="Lechuga", is_vegan=True, is_gluten_free=True, is_kosher=True
        )
        self.ingrediente2 = Ingrediente.objects.create(
            nombre="Pollo", is_vegan=False, is_gluten_free=True, is_kosher=False
        )
        self.ingrediente3 = Ingrediente.objects.create(
            nombre="Tomate", is_vegan=True, is_gluten_free=True, is_kosher=True
        )
        self.url_api = '/api/v1/platos/'

        self.nuevo_plato = {
            'nombre': 'Ensalada César v2',
            'ingredientes': [self.ingrediente1.id, self.ingrediente2.id]
        }

    def test_crear_plato(self):
        response = self.client.post(self.url_api, self.nuevo_plato, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        plato = Plato.objects.get(id=response.data['id'])
        self.assertEqual(plato.nombre, self.nuevo_plato['nombre'])
        self.assertEqual(plato.ingredientes.count(), len(self.nuevo_plato['ingredientes']))
        
        ingredientes_ids = [ing.id for ing in plato.ingredientes.all()]
        self.assertEqual(sorted(ingredientes_ids), sorted(self.nuevo_plato['ingredientes']))

    def test_plato_vegan(self):
        nuevo_plato_vegan = {
            'nombre': 'Ensalada Vegana',
            'ingredientes': [self.ingrediente1.id, self.ingrediente3.id]
        }

        response = self.client.post(self.url_api, nuevo_plato_vegan, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        plato = Plato.objects.get(id=response.data['id'])
        self.assertTrue(plato.is_vegan)

    def test_plato_no_vegan(self):
        nuevo_plato_no_vegan = {
            'nombre': 'Ensalada No Vegana',
            'ingredientes': [self.ingrediente1.id, self.ingrediente2.id] 
        }
        response = self.client.post(self.url_api, nuevo_plato_no_vegan, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        plato = Plato.objects.get(id=response.data['id'])
        self.assertFalse(plato.is_vegan)
    
    def test_read_plato(self):
        response_create = self.client.post(self.url_api, self.nuevo_plato, format='json')
        plato_id = response_create.data['id']
        
        response = self.client.get(f"{self.url_api}{plato_id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], plato_id)
        self.assertEqual(response.data['nombre'], self.nuevo_plato['nombre'])
        self.assertEqual(len(response.data['ingredientes']), len(self.nuevo_plato['ingredientes']))
    
    def test_update_plato(self):
        response_create = self.client.post(self.url_api, self.nuevo_plato, format='json')
        plato_id = response_create.data['id']
        
        plato_actualizado = {
            'nombre': 'Ensalada César v4',
            'ingredientes': [self.ingrediente1.id, self.ingrediente3.id] 
        }
        
        response_update = self.client.put(f"{self.url_api}{plato_id}/", plato_actualizado, format='json')
        self.assertEqual(response_update.status_code, status.HTTP_200_OK)
        self.assertEqual(response_update.data['nombre'], plato_actualizado['nombre'])
        self.assertEqual(len(response_update.data['ingredientes']), len(plato_actualizado['ingredientes']))
    
    def test_delete_plato(self):
        response_create = self.client.post(self.url_api, self.nuevo_plato, format='json')
        plato_id = response_create.data['id']

        response_delete = self.client.delete(f"{self.url_api}{plato_id}/")
        self.assertEqual(response_delete.status_code, status.HTTP_204_NO_CONTENT)
        
        response_get = self.client.get(f"{self.url_api}{plato_id}/")
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)

