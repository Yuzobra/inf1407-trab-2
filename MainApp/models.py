from django.db.models import Model, CharField, IntegerField, DecimalField, EmailField, CharField, DateField, TextChoices
from django.utils.translation import gettext_lazy

class BoardGame(Model):
    class GameState(TextChoices):
        NEW = 'NEW', gettext_lazy('New')
        USED = 'USED', gettext_lazy('Used')
        DEGRADED = 'DEGRADED', gettext_lazy('Degraded')

    name = CharField(max_length=100)
    release_year = IntegerField()
    price = DecimalField(decimal_places=2, max_digits=8)
    state = CharField(max_length=8, choices=GameState.choices)
    image_url = CharField(max_length=255)
    announce_date = DateField()

    