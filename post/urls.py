from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home, name= 'home'),
    path('post/<int:pk>/', views.Post_details, name='details'),
    path('post/<int:pk>/comment/', views.PostComment, name='comment'),
]
