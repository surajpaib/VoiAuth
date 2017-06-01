# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from forms import SpeakerForm
from models import SpeakerModel
# Create your views here.


def input(request):
    s = SpeakerForm()
    return render(request, 'train.html', {'form': s})


def train(request):
    if request.method == 'POST':
        form = SpeakerForm(request.POST)
        if form.is_valid():
            name_val = form.cleaned_data['name']
            sample = form.cleaned_data['sample']
            s = SpeakerModel()
            s.name = name_val
            s.sample = sample
            s.save()
            return HttpResponse('Train successful')

    else:
        s = SpeakerForm()
        render(request, 'train.html', {'form': s})

def authenticate(request):
    return HttpResponse('Authentication file page')
