from django.shortcuts import render
from django.http import HttpResponse
from .models import ControllerInput
import json
from django.views.decorators.csrf import csrf_exempt

import sys
sys.path.append('..')

from sensors.models import SensorData

# Create your views here.

def index(request):
    return HttpResponse(ControllerInput.objects.get(id=1))

def get(request):
    return HttpResponse(json.dumps(ControllerInput.objects.get(id=1).createDictionary()))

@csrf_exempt
def update(request, dictionary):
    d = json.loads(dictionary)
    controller = ControllerInput.objects.get(id=1)

    #print(controller.a)
    #c = ControllerInput.objects.get(id=1)
    #print(d['a'])
    for item in d:
        setattr(controller, item, d[item])
    controller.save() #need to make sure to save the object to the server
    #print(controller.a)
    return HttpResponse(json.dumps(SensorData.objects.get(id=1).createDictionary()))
