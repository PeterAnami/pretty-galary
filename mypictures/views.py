from django.shortcuts import render
from django.http.response import Http404, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')
