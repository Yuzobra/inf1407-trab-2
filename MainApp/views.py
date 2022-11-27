from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy

from MainApp.forms import BoardGameForm
from MainApp.models import BoardGame, Purchase
from MainApp.controllers import get_available_ads, get_ads_from_user, get_user_purchases

def register(req):
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )
            login(req, new_user)
            return redirect('homepage')
    else:
        form = UserCreationForm()
    context = {'form': form}

    return render(req, "register/register.html", context)

class BoardGameCRUD():
    @login_required
    def form(req):
        if req.method == "POST" and req.user.is_authenticated:  
            form = BoardGameForm(req.POST)
            if form.is_valid(): 
                try:
                    model_instance = form.save(commit=False)
                    model_instance.owner_id = req.user.id
                    form.save()  
                    return redirect(reverse_lazy("board_game_ads"))  
                except Exception as e:
                    print(e)
                    pass
            # else:
            #     errors = form.errors.as_json() 
            #     ...
        else:  
            form = BoardGameForm(initial={'owner': req.user.id})  
        return render(req,'board/board_games.html', {'form':form})  

    def list(req):
        ads = get_available_ads(req)
        return render(req, 'board/list.html', {'ads': ads}) 
        

    @login_required
    def edit(req, id):
        form = None
        context = {
            "title": "Atualize seu anúncio:",
            "button": "Atualizar" 
        }
        if req.method == "POST":
            board_game = BoardGame.objects.get(id=id)  
            form = BoardGameForm(req.POST, instance = board_game)  
            if form.is_valid():  
                form.save()
                return redirect(reverse_lazy("board_game_list"))  
            else:
                print(form.errors.as_data())
            context["form"] = form
        else:
            board_game = BoardGame.objects.get(id=id)
            form = BoardGameForm(instance=board_game)
            context["form"] = form
        return render(req,'board/board_games.html', context)

    @login_required
    def delete(req, id):  
        board_game = BoardGame.objects.get(id=id)  
        board_game.delete()  
        return redirect(reverse_lazy("homepage"))  

    @login_required
    def ads(req):
        ads = get_ads_from_user(req.user.id)
        return render(req, "board/ads.html", {'ads': ads})
    
class PurchasesCRUD():
    @login_required
    def purchase(req, id):
        board_game = BoardGame.objects.get(id=id)
        purchase = Purchase(
            buyer_id = req.user.id,
            seller = board_game.owner,
            game = board_game,
        )

        board_game.status = BoardGame.GameStatus.SOLD
        board_game.save()
        purchase.save()
        return redirect(reverse_lazy("board_game_list"))
    
    @login_required
    def list(req):
        purchases = get_user_purchases(req.user.id)
        return render(req, "board/purchases.html", {'purchases': purchases})
