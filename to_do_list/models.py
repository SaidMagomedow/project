from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Notes(models.Model):
    title = models.CharField(max_length=255)
    complete = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    data_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'