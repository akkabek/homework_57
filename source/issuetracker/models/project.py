from django.db import models


class Project(models.Model):
    begin_date = models.DateField(null=False, blank=False, verbose_name='Дата начала')
    end_date = models.DateField(null=True, blank=True, verbose_name='Дата окончания')
    title = models.CharField(null=False, blank=False, max_length=100, verbose_name='Название')
    description = models.TextField(null=False, blank=False, max_length=500, verbose_name='Описание')

    def __str__(self):
        return self.title