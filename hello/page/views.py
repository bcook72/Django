# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render


def profile(request):
    data = {
        'Message': 'Hello World!'
    }
    return JsonResponse(data)

def index(request):
    return render(request, 'page/index.html')
