from django.contrib import admin

# Register your models here.
from to_do_list.models import Notes


@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'description', 'complete', 'data_created', 'user'
    ]