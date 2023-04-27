from django.urls import path, include

from user import views


app_name = "user"

urlpatterns = [
    path('login-admin/', views.login_admin, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register-user/',views.register,name='register-user'),
    path('login-user/',views.login_user,name='login-user'),

]