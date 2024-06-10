from django.db import models


class Poster(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='sliders/')
    def __str__(self):
        return self.name
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


class ReviewBooks(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE,
                             related_name='review_books')
    text = models.TextField()
    mark = models.IntegerField(default=5)

    def __str__(self):
        return f'{self.book} - {self.mark}'


class Tags(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Product(models.Model):
    title= models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField(default=100)
    tags = models.ManyToManyField(Tags)

    def __str__(self):
        return f'{self.title} - {self,print}'