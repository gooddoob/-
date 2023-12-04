from django.urls import path
from . import views

app_name = 'login'
urlpatterns = [
    # ex /login/
    path('', views.login, name='index'),
]