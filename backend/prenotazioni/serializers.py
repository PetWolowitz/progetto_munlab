from rest_framework import serializers
from .models import Prenotazione, Attivita, Disponibilita

class AttivitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attivita
        fields = '__all__'

class DisponibilitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disponibilita
        fields = '__all__'    

class PrenotazioneSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Prenotazione    
        fields = '__all__'