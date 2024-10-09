from django.shortcuts import render
from django.http import HttpResponse

def mainpage_view(request):
    return HttpResponse("اولین صفحه‌ی من")