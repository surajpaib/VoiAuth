# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from forms import SpeakerForm, AuthForm
from models import SpeakerModel, AuthModel
from scripts import ModuleML
import numpy as np
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
            model.svm_run()
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
    if request.method == 'POST':
        form = AuthForm(request.POST, request.FILES)
        if form.is_valid():
            label = int(request.POST['pick'])
            model = ModuleML()
            val, total, pred, counts, values = model.predict(request.FILES['audio'])
            conf = 0
            for idx, value in enumerate(values):
                if value == label:
                    conf = counts[idx] / total

            if pred == label:
                st = "Match"
            else:
                st = "No Match"

            person_true = SpeakerModel.objects.get(label= pred)
        else:
            list = SpeakerModel.objects.all()
            auth = AuthForm()
            return render(request, 'authenticate.html', {'form': auth, 'items': list})
    else:
        list = SpeakerModel.objects.all()
        auth = AuthForm()
        return render(request, 'authenticate.html', {'form': auth, 'items': list})
    return HttpResponse(st + '\n Confidence Score:\t'+ str(conf))