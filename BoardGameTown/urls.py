"""BoardGameTown URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
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
    path('board_game/update/<int:id>', views.BoardGameCRUD.update, name="board_game_update"),
    path('board_game/delete/<int:id>', views.BoardGameCRUD.delete, name="board_game_delete"),
    path('board_game/purchase/<int:id>', views.BoardGameCRUD.purchase, name="board_game_purchase"),
]
