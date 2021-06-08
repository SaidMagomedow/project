from django import forms

from to_do_list.models import Notes


class NoteCreateForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description', 'priority']
        labels = {
            'title': 'Название заметки',
            'description': 'Описание',
            'priority': 'Приоритет',
        }


class NoteUpdateForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['description', 'complete', 'priority']
        labels = {
            'complete': 'Выполнено',
            'priority': 'Приоритет',
            'description': 'Описание',
        }