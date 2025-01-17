
from django.contrib import admin
from django.urls import path, include
from auth_user import views as auth_user_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls')),
    path('register/', auth_user_view.Register, name="register"),
    path('login/', auth_user_view.UserLogin, name="login"),
    path('logout/', auth_user_view.UserLogout, name="logout")
]
