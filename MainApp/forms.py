from django.forms import ModelForm
from MainApp.models import BoardGame

class BoardGameForm(ModelForm):
    class Meta:
        model = BoardGame
        exclude = ['announce_date', 'owner', 'status']
        labels = {
            "name": "Nome",
            "release_year": "Ano de lançamento",
            "price": "Preço",
            "state": "Estado do jogo",
            "image_url": "Link da imagem" 
        }