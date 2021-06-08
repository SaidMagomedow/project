from django import forms

from to_do_list.models import Notes


class NoteCreateForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description']
        labels = {
            'title': 'Название заметки',
            'description': 'Описание'
        }


class NoteUpdateForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['complete']
        labels = {
            'complete': 'Выполнено'
        }