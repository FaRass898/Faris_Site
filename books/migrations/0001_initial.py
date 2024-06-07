# Generated by Django 5.0.6 on 2024-06-06 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Напишите название книги')),
                ('author_name', models.CharField(max_length=100, verbose_name='Напишите имя автора')),
                ('image', models.ImageField(upload_to='programming_blog/', verbose_name='Загрузите фото')),
                ('short_description', models.TextField(verbose_name='Напишите описание')),
                ('data_release', models.DateField(verbose_name='Укажите дату выхода книги')),
                ('genre', models.CharField(choices=[('ФЭНТЕЗИ', 'ФЭНТЕЗИ'), ('ФАНТАСТИКА', 'ФАНТАСТИКА'), ('БОЕВИКИ', 'БОЕВИКИ'), ('ДЕТЕКТИВ', 'ДЕТЕКТИВ'), ('ДРАМА', 'ДРАМА'), ('ХОРРОР', 'ХОРРОР')], max_length=100, verbose_name='Выберите жанр')),
                ('summary', models.FileField(upload_to='summary/', verbose_name='Загрузите  краткое содержание')),
                ('wiki', models.URLField(verbose_name='Вставьте сыллку на википедию')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='')),
            ],
        ),
    ]