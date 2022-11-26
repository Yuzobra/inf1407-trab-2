from django.forms import ModelForm
from MainApp.models import BoardGame

class BoardGameForm(ModelForm):
    class Meta:
        model = BoardGame
        fields = "__all__"
