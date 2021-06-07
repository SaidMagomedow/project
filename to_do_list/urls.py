from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from to_do_list.views import NoteListView

app_name = 'to_do_list'

urlpatterns =[
    path('note-list/', NoteListView.as_view(), name='note-list'),
]
