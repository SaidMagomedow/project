from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView
from django.contrib.auth.forms import AuthenticationForm


class RegistredView(CreateView):
    template_name = 'signup.html'
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse_lazy('to_do_list:note-list')

