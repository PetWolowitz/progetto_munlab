from django.urls import path, include
from rest_framework import routers
from .views import AttivitaViewSet, PrenotazioneViewSet, DisponibilitaViewSet

router = routers.DefaultRouter()
router.register(r'attivita', AttivitaViewSet)
router.register(r'prenotazioni', PrenotazioneViewSet)
router.register(r'disponibilita', DisponibilitaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
