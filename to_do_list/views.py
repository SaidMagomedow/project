from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from to_do_list.forms import NoteCreateForm, NoteUpdateForm
from to_do_list.models import Notes


class NoteListView(ListView):
    model = Notes
    template_name = 'notes_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = Notes.objects.all()
        if status := self.request.GET.get('priority'):
            print(status)
        if status := self.request.GET.get('complete_status'):
            context['notes'] = Notes.objects.filter(complete=status)
# context['notes'] = Notes.objects.all()
#         context['notes'] = Notes.objects.all()
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


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Notes
    success_url = reverse_lazy('to_do_list:note-list')