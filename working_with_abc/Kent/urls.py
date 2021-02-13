from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage),
    path('info/',views.index),
    path('address/',views.address),
    path('address/hello/',views.hello),
    path('login/',views.login),
    path('signup/',views.signup),
    path('login/signup/',views.signup),
    path('form/', views.get_request),

]