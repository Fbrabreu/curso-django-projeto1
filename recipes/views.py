from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return HttpResponse('HOME')



def contato(request):
    return HttpResponse('CONTATO')
    # return Http response

def sobre(request):
    return HttpResponse('SOBRE:')
    # return Http response