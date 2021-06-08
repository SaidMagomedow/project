from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from to_do_list.forms import NoteCreateForm, NoteUpdateForm
from to_do_list.models import Notes


class NoteListView(LoginRequiredMixin, ListView):
    model = Notes
    template_name = 'notes_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = Notes.objects.all().order_by('-data_created')
        context['form'] = NoteCreateForm()
        context['form_update'] = NoteUpdateForm()
        return context


class NoteCreateView(LoginRequiredMixin, CreateView):
    form_class = NoteCreateForm
    model = Notes
    template_name = 'notes_list.html'
    success_url = reverse_lazy('to_do_list:note-list')


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    form_class = NoteUpdateForm
    model = Notes
    success_url = reverse_lazy('to_do_list:note-list')


class NoteDeleteView(DeleteView):
    model = Notes
    success_url = reverse_lazy('to_do_list:note-list')