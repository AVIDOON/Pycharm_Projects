from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('login',views.login),
    path('signup',views.signup),
    path('login/welcome',views.welcome),
    path('signup/goToLogin',views.goToLogin)




]

# login ->  Welcome
# signup -> Go to Login