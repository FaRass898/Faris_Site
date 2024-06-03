from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import random

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

