from base import views
from django.urls import path

urlpatterns = [
   path('',views.index,name="index.html"),
   path('chatai/',views.chat,name="chatai"),
    
]