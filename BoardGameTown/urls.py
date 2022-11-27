from django.contrib import admin
from django.urls import path
from django.urls.base import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from MainApp import views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.BoardGameCRUD.list, name="homepage"),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='register/login.html', next_page=reverse_lazy("homepage")), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('homepage')), name='logout'),
    path('board_game', views.BoardGameCRUD.form, name="board_game"),
    path('board_game/list', views.BoardGameCRUD.list, name="board_game_list"),
    path('board_game/ads', views.BoardGameCRUD.ads, name="board_game_ads"),
    path('board_game/edit/<int:id>', views.BoardGameCRUD.edit, name="board_game_edit"),
    path('board_game/delete/<int:id>', views.BoardGameCRUD.delete, name="board_game_delete"),
    path('board_game/purchase', views.PurchasesCRUD.list, name="purchase_list"),
    path('board_game/purchase/<int:id>', views.PurchasesCRUD.purchase, name="purchase"),
]
