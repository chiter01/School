from django.urls import path
from . import views

urlpatterns = [
    path('create_news/', views.create_news, name='create_news'),
    path('delete/<int:id>/', views.delete_news, name='delete_news'),
    path('ubdate/<int:id>/', views.ubdate_news, name='ubdate_news'),
    path('login/', views.login_profile, name='login'),
    path('logout/', views.logout_profile, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/change-password/', views.change_password, name='change_password'),
    path('', views.workspace, name='workspace'),
]