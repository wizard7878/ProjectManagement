from django.urls import path, include

from . import views

urlpatterns = [
    path('sign_up', views.UserSignUpView.as_view(), name = 'sign_up'),
    path('login/', views.UserLoginView.as_view(), name = 'login'),
    path('logout/', views.user_logout, name='logout'),
]