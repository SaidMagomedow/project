from django.urls import include, path
from django.contrib.auth import views as auth_views

from registration.views import RegistredView

app_name = 'registration'

urlpatterns =[
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', RegistredView.as_view(), name='register')
]