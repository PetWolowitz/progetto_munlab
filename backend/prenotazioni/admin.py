from django.contrib import admin
from .models import Attivita, Disponibilita, Prenotazione

# Register your models here.

admin.site.register(Attivita)
admin.site.register(Disponibilita)
admin.site.register(Prenotazione)
