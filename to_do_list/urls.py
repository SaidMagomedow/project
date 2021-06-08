from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from to_do_list.views import NoteListView, NoteCreateView, NoteUpdateView, NoteDeleteView

app_name = 'to_do_list'

urlpatterns =[
    path('', NoteListView.as_view(), name='note-list'),
    path('note-create/', NoteCreateView.as_view(), name='note-create'),
    path('note-update/<int:pk>/', NoteUpdateView.as_view(), name='note-update'),
    path('note-delete/<int:pk>/', NoteDeleteView.as_view(), name='note-delete')

]
