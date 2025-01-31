from django.urls import path, include

from .views import PlatoViewSet, IngredienteViewSet, SlackWebhookView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('ingredientes', IngredienteViewSet)
router.register('platos', PlatoViewSet)

urlpatterns = [
    path('slack-webhookview/', SlackWebhookView.as_view()),
    path('', include(router.urls)),
]