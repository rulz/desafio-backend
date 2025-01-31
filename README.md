## Instalación de Requerimientos del Proyecto

Para instalar los requerimientos del proyecto en tu entorno local, ejecuta el siguiente comando:

```
pip install -r requirements_test.txt
```

### Comandos Disponibles en `fabfile.py`

A continuación, se presentan algunos comandos útiles que puedes ejecutar desde `fabfile.py`:

```
fab ma                # Crear migraciones (makemigrations)
fab mi                # Aplicar migraciones (migrate)
fab createsuperuser   # Crear un usuario administrador
fab run               # Ejecutar el servidor de desarrollo
```

---

## Endpoints de Ejemplo

### Generar Token de Acceso

Para autenticarte y obtener un token de acceso para consumir la API, ejecuta el siguiente comando:

```
curl -X POST http://localhost:8000/api/token/ \
     -H "Content-Type: application/json" \
     -d '{"username": "admin", "password": "admin"}'
```

### Obtener Todos los Ingredientes y Platos

Utiliza el siguiente comando para obtener la lista de ingredientes y platos. Recuerda reemplazar `tu_token_aqui` con tu token real:

```
TOKEN="tu_token_aqui"

curl -X GET http://localhost:8000/api/v1/ingredientes/ \
     -H "Authorization: Bearer $TOKEN"

curl -X GET http://localhost:8000/api/v1/platos/ \
     -H "Authorization: Bearer $TOKEN"
```

### Crear un Nuevo Ingrediente

Para agregar un nuevo ingrediente, usa el siguiente comando:

```
TOKEN="tu_token_aqui"

curl -X POST http://localhost:8000/api/v1/ingredientes/ \
     -H "Authorization: Bearer $TOKEN" \
     -H "Content-Type: application/json" \
     -d '{
           "nombre": "Espárrago",
           "is_vegan": true,
           "is_gluten_free": true,
           "is_kosher": true
         }'
```

### Crear un Nuevo Plato

Para crear un nuevo plato con ingredientes específicos, usa el siguiente comando:

```
TOKEN="tu_token_aqui"

curl -X POST http://localhost:8000/api/v1/platos/ \
     -H "Authorization: Bearer $TOKEN" \
     -H "Content-Type: application/json" \
     -d '{
           "nombre": "Ensalada Cesar v14",
           "ingredientes": [1, 2]
         }'
```

### Eliminar un Plato

Para eliminar un plato específico, reemplaza `PLATO_ID` con el ID del plato que deseas eliminar y ejecuta el siguiente comando:

```
TOKEN="tu_token_aqui"
PLATO_ID=7  # Reemplaza con el ID real

curl -X DELETE http://localhost:8000/api/v1/platos/$PLATO_ID/ \
     -H "Authorization: Bearer $TOKEN" \
     -H "Content-Type: application/json"
```

---

## Integración con Slack

### Configuración

Para usar la integración con Slack, necesitas obtener un token de acceso desde tu cuenta de Slack. Agrega las siguientes variables de entorno en `settings.py`:

```
SLACK_TOKEN = os.getenv('SLACK_TOKEN', '<replace-this>')
SLACK_CHANNEL = os.getenv('SLACK_CHANNEL', '<replace-this>')
```

### Enviar un Mensaje a Slack

Para enviar un mensaje a Slack simulando una solicitud `POST`, usa el siguiente comando:

```
URL="http://localhost:8000/api/v1/slack-webhookview/"

curl -X POST $URL \
     -H "Content-Type: application/json" \
     -d '{
           "text": "platos"
         }'
```

---

Este documento proporciona una guía rápida para la instalación y el uso de los principales endpoints del proyecto. Asegúrate de reemplazar los valores de ejemplo con los datos reales antes de ejecutar los comandos.

