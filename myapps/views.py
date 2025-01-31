from rest_framework import viewsets, mixins, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

from . import models
from . import serializers

from utils import slack
import json

class IngredienteViewSet(viewsets.ModelViewSet):
    queryset = models.Ingrediente.objects.all()
    serializer_class = serializers.IngredienteSerializer

class PlatoViewSet(viewsets.ModelViewSet):
    queryset = models.Plato.objects.prefetch_related('ingredientes')

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return serializers.PlatoSerializer
        return serializers.PlatoDetailSerializer

class SlackWebhookView(APIView):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        text = data.get("text", "").lower()
        
        if "platos" in text:
            platos = models.Plato.objects.all()
            response_text = "Platos disponibles:\n" + "\n".join([p.nombre for p in platos])
            slack.slack_send(response_text)
            return Response({"text": response_text}, status=status.HTTP_200_OK)
        return Response({"text": "Comando no reconocido"}, status=status.HTTP_400_BAD_REQUEST)
