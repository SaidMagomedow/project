from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class Notes(models.Model):

    STATUS_CHOISES = {
        (COMPLETE := 'COMPLETE', 'Готово'),
        (IN_PROGRESS := 'IN_PROGRESS', 'Выполняется'),
        (POSTPONED := 'POSTPONED', 'Отложено')
    }

    PRIORITY_CHOISES = {
        (UN_IMPORTANT := 'UN_IMPORTANT', 'Неважный'),
        (IMPORTANT := 'IMPORTANT', 'Важный'),
        (VERY_IMPORTANT := 'VERY_IMPORTANT', 'Очень важный')
    }

    title = models.CharField(max_length=255)
    complete = models.CharField(max_length=25, default=IN_PROGRESS, choices=STATUS_CHOISES)
    priority = models.CharField(max_length=25, choices=PRIORITY_CHOISES)
    description = models.TextField(null=True, blank=True)
    data_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        ordering = ['-data_created']