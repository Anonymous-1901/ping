from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_user),
    path('login/',views.login_user,name='login'),
    path('login/login_required',views.login_user,name='login_required'),
    path('logout',views.logout_user,name='logout'),
    path('chat/',views.chat,name='chat'),
    path(r'chat/<username>',views.chat,name='chat_user'),
    path('search',views.search,name='search'),
    path(r'user/<user>',views.user,name='user')
]
