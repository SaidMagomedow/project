from django.urls import include, path
from django.contrib.auth import views as auth_views

from registration.views import RegistredView, SomeLoginView

app_name = 'registration'

urlpatterns =[
    path('login/', SomeLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', RegistredView.as_view(), name='register')
]