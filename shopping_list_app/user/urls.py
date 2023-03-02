from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
    path('user/<int:user_id>/', views.personal_area, name='personal_area'),
    path('create_list', views.create_list, name='create_list'),
    path('delete_list/<int:list_id>/', views.delete_list, name='delete_list'),
    path('manage/<int:list_id>/', views.manage_list, name='manage_list')

]