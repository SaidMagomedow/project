from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView
from django.contrib.auth.forms import AuthenticationForm


class RegistredView(FormView):
    template_name = 'registration.html'
    form_class = UserCreationForm

    def form_valid(self, form):
        create = form.save()
        if create is not None:
            login(self.request, create)
        return super(RegistredView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('to_do_list:main')


class SomeLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm

    def get_success_url(self):
        return reverse_lazy('to_do_list:main')
