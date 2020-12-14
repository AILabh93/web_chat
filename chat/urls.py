from django.urls import path
from . import views
urlpatterns = [
    path('', views.login, name = 'login'),
    path('chat/', views.Home.as_view(), name = 'home'),
    path('chat/content/', views.get_chat_content, name = 'chat_content'),
]
