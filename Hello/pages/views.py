from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homePageView(request):
    return HttpResponse('<h3>Hello, This is Sushrut Rajesh Babhulkar from T1 Batch and my PRN is 1841003</h3>')
