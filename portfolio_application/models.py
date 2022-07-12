from django.db import models


class Skill(models.Model):
    class Meta():
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'
    title = models.CharField(verbose_name='Название навыка', max_length=100)
    description = models.TextField(verbose_name='Описание навыка')
    picture = models.ImageField(verbose_name='Картинка навыка')

    def __str__(self):
        return f'{self.title} {self.description}'


class Project(models.Model):
    class Meta():
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
    title = models.CharField(verbose_name='Название проекта', max_length=100)
    description = models.TextField(verbose_name='Описание проекта')
    picture = models.ImageField(verbose_name='Картинка проекта')
    link_project = models.URLField(verbose_name='Адрес проекта')

    def __str__(self):
        return f'{self.title} {self.description} {self.link_project}'
