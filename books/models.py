from django.db import models

class Books(models.Model):

    GENRE_CHOICES = (
        ('ФЭНТЕЗИ','ФЭНТЕЗИ'),
        ("ФАНТАСТИКА","ФАНТАСТИКА"),
        ("БОЕВИКИ", "БОЕВИКИ"),
        ("ДЕТЕКТИВ", "ДЕТЕКТИВ"),
        ("ДРАМА", "ДРАМА"),
        ("ХОРРОР", "ХОРРОР"),

    )
    name = models.CharField(max_length=100, verbose_name='Напишите название книги')
    author_name = models.CharField(max_length=100, verbose_name='Напишите имя автора')

    image = models.ImageField(upload_to='programming_blog/', verbose_name='Загрузите фото')
    short_description = models.TextField(verbose_name='Напишите описание')
    data_release = models.DateField(verbose_name='Укажите дату выхода книги')
    genre = models.CharField(max_length=100, verbose_name='Выберите жанр',
                             choices=GENRE_CHOICES)
    summary = models.FileField(upload_to='summary/', verbose_name='Загрузите  краткое содержание')
    wiki = models.URLField(verbose_name='Вставьте сыллку на википедию')
    created_at = models.DateField(auto_now_add=True, verbose_name='')

    class Meta:
        verbose_name = 'Книгу'
        verbose_name_plural = 'Книги'