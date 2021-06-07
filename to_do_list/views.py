from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import ListView

from to_do_list.models import Notes


class NoteListView(ListView):
    model = Notes
