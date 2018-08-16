from django.shortcuts import render
from django.http import HttpResponse

def company_basic(request, ticker):
    return HttpResponse("You're looking at company %s." % ticker)
