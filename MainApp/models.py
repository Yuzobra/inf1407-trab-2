from django.db.models import Model, CharField, IntegerField, DecimalField, ForeignKey, CharField, DateField, TextChoices, DateTimeField
from django.db.models import F, Q, CheckConstraint, CASCADE

from django.conf import settings
from django.utils.translation import gettext_lazy
from django.utils.timezone import now

class BoardGame(Model):
    class GameState(TextChoices):
        NEW = 'NEW', gettext_lazy('New')
        USED = 'USED', gettext_lazy('Used')
        DEGRADED = 'DEGRADED', gettext_lazy('Degraded')

    class GameStatus(TextChoices):
        AVAILABLE = 'AVAILABLE', gettext_lazy("Available")
        SOLD = 'SOLD', gettext_lazy('Sold')

    name = CharField(max_length=100)
    release_year = IntegerField()
    price = DecimalField(decimal_places=2, max_digits=8)
    state = CharField(max_length=8, choices=GameState.choices)
    image_url = CharField(max_length=255)
    announce_date = DateField(default=now)
    owner = ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=CASCADE,
    )
    status = CharField(max_length=9, choices=GameStatus.choices, default='AVAILABLE')

class Purchase(Model):
    game = ForeignKey(
        BoardGame,
        on_delete=CASCADE
    )
    buyer = ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=CASCADE,
        related_name='buyer'
    )
    seller = ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=CASCADE,
        related_name='seller'
    )
    timestamp = DateTimeField(default=now)
    

    class Meta:
        constraints = [
            CheckConstraint(name='not_same', check=~Q(buyer=F('seller')))
        ]