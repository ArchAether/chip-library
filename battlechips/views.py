from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse

import csv

# Create your views here.
def mmbn6_all(request):
    battlechips = []
    with open('battlechips/static/csvs/StandardBattleChips.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            battlechips.append({'number': int(row[0]), 'name': row[2], 'damage': row[4], 'description': row[5], 'location': row[6]})
    return JsonResponse(battlechips, safe=False)