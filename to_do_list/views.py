from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect

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
        priority = self.request.GET.get('priority_status')
        complete = self.request.GET.get('complete_status')
        context['form_create'] = NoteCreateForm()
        context['form_update'] = NoteUpdateForm()
        user = self.request.user
        if user.is_superuser:
            context['notes'] = Notes.objects.all()
            if priority or complete:
                context['notes'] = Notes.objects.filter(
                    Q(priority=priority) | Q(complete=complete))
        else:
            context['notes'] = Notes.objects.filter(user_id=user.pk)
            if priority or complete:
                context['notes'] = Notes.objects.filter(
                    Q(priority=priority, user_id=user.pk) | Q(complete=complete, user_id=user.pk))
        return context


class NoteCreateView(LoginRequiredMixin, CreateView):
    form_class = NoteCreateForm
    model = Notes
    template_name = 'notes_list.html'
    success_url = reverse_lazy('to_do_list:note-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user_id = self.request.user.pk
        self.object.save()
        return redirect('to_do_list:note-list')


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    form_class = NoteUpdateForm
    model = Notes
    success_url = reverse_lazy('to_do_list:note-list')


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Notes
    success_url = reverse_lazy('to_do_list:note-list')