from django.forms import ModelForm
from MainApp.models import BoardGame

class BoardGameForm(ModelForm):
    class Meta:
        model = BoardGame
        exclude = ['announce_date', 'owner']