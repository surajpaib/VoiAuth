# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from models import SpeakerModel
# Create your views here.

def train(request):
    s = SpeakerModel(name= 'Suraj')
    return render(request, 'train.html', context={ 'model': s})
    

def authenticate(request):
    return HttpResponse('Authentication file page')
