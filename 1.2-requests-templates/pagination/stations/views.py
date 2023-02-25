import csv
from _csv import reader

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


content = []


def bus_stations(request):

    page_number = int(request.GET.get('page', 1))
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open('data-398-2018-08-30.csv', encoding='utf-8', newline='') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            content.append(row)

    paginator = Paginator(content, 10)
    page = paginator.get_page(page_number)

    context = {
         'bus_stations': page,
         'page': page,
    }
    return render(request, 'stations/index.html', context)
