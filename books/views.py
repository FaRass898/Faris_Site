from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
import random
from books.models import Books



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

