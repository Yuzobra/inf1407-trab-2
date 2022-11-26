from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy

from MainApp.forms import BoardGameForm
from MainApp.models import BoardGame

def homepage(req):
    return render(req, "home.html")

def segundaPagina(req):
    return HttpResponse("Hello")

def register(req):
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = UserCreationForm()
    context = {'form': form}

    return render(req, "register/register.html", context)

class BoardGameCRUD():
    @login_required
    def form(req):
        if req.method == "POST":  
            form = BoardGameForm(req.POST)  
            if form.is_valid():  
                try:  
                    form.save()  
                    return redirect(reverse_lazy("board_game_list"))  
                except:  
                    pass  
        else:  
            form = BoardGameForm()  
        return render(req,'board/board_games.html',{'form':form})  

    def list(req):
        board_games = BoardGame.objects.all()
        return render(req, "board/list.html", {'board_games': board_games})

    @login_required
    def edit(req, id):
        board_game = BoardGame.objects.get(id=id)
        return render(req,'board/edit.html', {'board_game': board_game}) 

    @login_required
    def update(req, id):  
        board_game = BoardGame.objects.get(id=id)  
        form = BoardGameForm(req.POST, instance = board_game)  
        if form.is_valid():  
            form.save()  
            return redirect(reverse_lazy("list"))  
        return render(req, 'board/edit.html', {'board_game': board_game}) 

    @login_required
    def delete(req, id):  
        board_game = BoardGame.objects.get(id=id)  
        board_game.delete()  
        return redirect(reverse_lazy("homepage"))  

    