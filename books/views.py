from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
import random
from books.models import Books
from . import forms
#fff

def edit_books_view(request, id):
        book_id = get_object_or_404(Books, id=id)
        if request.method == 'POST':
                form = forms.BookForm(request.POST, instance=book_id)
                if form.is_valid():
                        form.save()
                        return HttpResponse('<h3>Book Created</h3>'
                                            '<a href="/books/books_catalog">На список сотрудников</a>')
        else:
                form = forms.BookForm(instance=book_id)
        return render(request, template_name='blog/edit_book.html',
                      context={'form':form,
                               'book_id': book_id
                               })

def drop_books_view(request, id):
        book_id = get_object_or_404(Books, id=id)
        book_id.delete()
        return HttpResponse('Book deleted <a href="/books/books_catalog">На список сотрудников</a>')

def create_books_view(request):
        if request.method == 'POST':
                form = forms.BookForm(request.POST, request.FILES)
                if form.is_valid():
                        form.save()
                        return HttpResponse('<h3>Book Created</h3>'
                                            '<a href="/books/books_catalog">На список сотрудников</a>')
        else:
                form = forms.BookForm()

        return render(request, template_name='blog/create_books.html',
                      context={'form': form})


def books_list_view(request):
        if request.method == 'GET':
                query = Books.objects.filter().order_by('-id')
                return render(
                        request,
                        template_name="blog/books_list.html",
                        context={
                                'books' : query
                        }
                )

def books_detail_view(request, id):
        if request.method == 'GET':
                book_id = get_object_or_404(Books, id=id)
                return render(
                        request,
                        template_name="blog/books_detail.html",
                        context={
                                "book_id" : book_id
                        }
                )



def personal_info_view(request):

        return HttpResponse("Ваше имя: Фарис, Возраст: 17")

def hobby_view(request):

        return HttpResponse("Мое хобби: чтение книг")

def current_time_view(request):

        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return HttpResponse(f"Текущее время: {now}")

def random_numbers_view(request):

        numbers = random.sample(range(1, 100), 5)
        return HttpResponse(f"Случайные числа: {', '.join(map(str, numbers))}")

