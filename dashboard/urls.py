from django.urls import path

from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', views.accounts, name='accounts'),
    path('accounts/new/', views.add_account, name='add_account'),
    path('', views.profile, name='profile')
]
