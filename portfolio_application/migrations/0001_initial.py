# Generated by Django 4.0.5 on 2022-07-14 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название проекта')),
                ('description', models.TextField(verbose_name='Описание проекта')),
                ('picture', models.FileField(blank=True, null=True, upload_to='portfolio_application/img', verbose_name='Картинка проекта')),
                ('link_project', models.URLField(verbose_name='Адрес проекта')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название навыка')),
                ('description', models.TextField(verbose_name='Описание навыка')),
                ('picture', models.FileField(blank=True, null=True, upload_to='portfolio_application/img', verbose_name='Картинка навыка')),
            ],
            options={
                'verbose_name': 'Навык',
                'verbose_name_plural': 'Навыки',
            },
        ),
    ]
