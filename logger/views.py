from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse

def log_index(request):
    return render(request, 'log_index.html')

def log_info(request):
    if request.method == 'POST':
        return HttpResponse(status=405)
    name = request.GET.get('name')
    if name is None:
        return HttpResponse('No name!')
    return JsonResponse({'chat': name, 'messages': 88})


def log_create(request):
    if request.method != 'POST':
        return HttpResponse(status=405)
    name = request.GET.get('name')
    if name is None:
        return HttpResponse('No name!')
    else:
        return JsonResponse({'chat': name, 'messages': 0})


def log_list(request):
    if request.method == 'POST':
        return HttpResponse(status=405)
    return JsonResponse({1: 'Inokentii', 2: 'Evdokim'})