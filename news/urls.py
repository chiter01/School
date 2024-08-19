from django.urls import path
from . import views


urlpatterns = [  
    path('<int:id>/', views.detail_news, name='detail_news'),
    path('index_new/', views.index_new, name='index_new'),
    path('', views.main, name='main'),
]