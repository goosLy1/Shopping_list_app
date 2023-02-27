from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout')

]