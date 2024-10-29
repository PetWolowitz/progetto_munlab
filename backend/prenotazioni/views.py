from django.shortcuts import render
from .models import Prenotazione, Attivita, Disponibilita
from .serializers import AttivitaSerializer, PrenotazioneSerializer, DisponibilitaSerializer
from rest_framework import viewsets, permissions

# Create your views here.
class AttivitaViewSet(viewsets.ModelViewSet):
    queryset = Attivita.objects.all()
    serializer_class = AttivitaSerializer
    permission_classes = [permissions.AllowAny]  # Accesso aperto

class PrenotazioneViewSet(viewsets.ModelViewSet):
    queryset = Prenotazione.objects.all()
    serializer_class = PrenotazioneSerializer
    permission_classes = [permissions.IsAuthenticated]  # Solo utenti autenticati

class DisponibilitaViewSet(viewsets.ModelViewSet):
    queryset = Disponibilita.objects.all()
    serializer_class = DisponibilitaSerializer
    permission_classes = [permissions.AllowAny]  # Accesso aperto