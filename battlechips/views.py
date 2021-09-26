import battlechips
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse

import csv

# Create your views here.
def mmbn6_all(request):
    battlechips = get_battleChips()
    return JsonResponse(battlechips, safe=False)

def mmbn_by_name(request, name):
    battlechips = get_battleChips()
    results = []
    for chip in battlechips:
        if name.lower() in chip.get('name').lower():
            results.append(chip)
    return JsonResponse(results, safe=False)

def mmbn6_by_id(request, id_number):
    battlechips = get_battleChips()
    result = None
    for chip in battlechips:
        if chip.get('number') == id_number:
            result = chip
    return JsonResponse(result)

def mmbn6_by_elem(request, elem):
    battlechips = get_battleChips()
    results = []
    for chip in battlechips:
        if chip.get('type') == elem.lower():
            results.append(chip)
    return JsonResponse(results, safe=False)

def mmbn6_by_description(request, description):
    battlechips = get_battleChips()
    result = []
    for chip in battlechips:
        if description.lower() in chip.get('description').lower():
            result.append(chip)
    return JsonResponse(result, safe=False)

def get_battleChips():
    battlechips = []
    with open('battlechips/static/csvs/MMBN6-BattleChips.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            battlechips.append({'number': int(row[0]), 'name': row[2], 'type': row[3], 'damage': row[4], 'description': row[5], 'location': row[6]})
    return battlechips