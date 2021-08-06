from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


@require_POST
@csrf_exempt
def example(request):
	return HttpResponse('Hello, world. This is the webhook response.')

@csrf_exempt
def webhooks(request):
    print(json.loads(request.body))
    #print(str(request)[71:80])
    return HttpResponse('',status=200)


@csrf_exempt
def webhookstest(request):
    print(json.loads(request.body))
    #print(str(request)[71:80])
    return HttpResponse('',status=200)
