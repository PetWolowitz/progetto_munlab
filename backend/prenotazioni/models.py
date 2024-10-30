from django.db import models
from django.contrib.auth.models import User

class Attivita(models.Model):
    # Definizione delle scelte per il tipo di attività
    TIPO_ATTIVITA = [
        ('EDU', "Educativa"),
        ('DOM', "Domenicale"),
        ('ALT', "Altro"),
    ]

    # Campi del modello Attivita
    nome = models.CharField(max_length=100)
    descrizione = models.TextField()
    costo = models.DecimalField(max_digits=6, decimal_places=2)
    durata = models.DurationField()
    posti_massimi = models.PositiveIntegerField()
    tipo = models.CharField(max_length=3, choices=TIPO_ATTIVITA)

    def __str__(self):
        
        return self.nome


class Prenotazione(models.Model):
    # Definizione degli stati possibili per una prenotazione
    STATO_PRENOTAZIONE = [
        ('CON', 'Confermata'),
        ('ATT', 'In Attesa'),
        ('CAN', 'Cancellata'),
    ]

    # Campi del modello Prenotazione
    utente = models.ForeignKey(User, on_delete=models.CASCADE)
    attivita = models.ForeignKey(Attivita, on_delete=models.CASCADE)
    data = models.DateField()
    stato = models.CharField(max_length=3, choices=STATO_PRENOTAZIONE, default='ATT')
    numero_partecipanti = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.attivita.nome} - {self.data} - {self.utente.username}"


class Disponibilita(models.Model):
    # Campi del modello Disponibilita
    attivita = models.ForeignKey(Attivita, on_delete=models.CASCADE)
    data = models.DateField()
    posti_disponibili = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.attivita.nome} - {self.data} - {self.posti_disponibili} posti disponibili"
