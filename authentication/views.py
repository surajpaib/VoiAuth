# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from forms import SpeakerForm, AuthForm
from models import SpeakerModel, AuthModel
from scripts import ModuleML
# Create your views here.


def input(request):
    s = SpeakerForm()
    return render(request, 'train.html', {'form': s})


def train(request):
    if request.method == 'POST':
        form = SpeakerForm(request.POST, request.FILES)
        if form.is_valid():
            name_val = form.cleaned_data['name']
            model = ModuleML()
            train_x, train_y, label = model.train_model(request.FILES['audio'])
            s = SpeakerModel()
            s.audio = 0
            s.name = name_val
            s.label = label
            s.save()
            return HttpResponse('Training successful')
        else:
            s = SpeakerForm()
            render(request, 'train.html', {'form': s})

    else:
        s = SpeakerForm()
        render(request, 'train.html', {'form': s})

def authenticate(request):
    list = SpeakerModel.objects.all()
    auth = AuthForm()
    return render(request, 'authenticate.html', {'form': auth , 'items': list})

def result(request):
    return HttpResponse('tested')