from django.db import models

from django.contrib.auth import get_user_model


class Project(models.Model):
    begin_date = models.DateField(null=False, blank=False, verbose_name='Дата начала')
    end_date = models.DateField(null=True, blank=True, verbose_name='Дата окончания')
    title = models.CharField(null=False, blank=False, max_length=100, verbose_name='Название')
    description = models.TextField(null=False, blank=False, max_length=500, verbose_name='Описание')

    users = models.ManyToManyField(
        get_user_model(),
        related_name='projects',
        blank=True,
        verbose_name='Участники'
    )

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ("manage_users", "Can manage project users"),
        ]