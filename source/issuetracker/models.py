from django.db import models

class Status(models.Model):
    name = models.CharField(null=False, blank=False, max_length=50, verbose_name='Название')

class Type(models.Model):
    name = models.CharField(null=False, blank=False, max_length=50, verbose_name='Название')

class Task(models.Model):
    summary = models.CharField(null=False, blank=False, max_length=500, verbose_name='Краткое описание')
    description = models.CharField(null=True, blank=True, max_length=500, verbose_name='Подробное описание')
    status = models.ForeignKey(Status, on_delete=models.RESTRICT, verbose_name='Статус')
    type = models.ForeignKey(Type, on_delete=models.RESTRICT, verbose_name='Тип')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
