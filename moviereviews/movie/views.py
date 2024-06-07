from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse('<h2>witam na stronie glownej</h2>')

def about(request):
    return HttpResponse('<h1>Strona o mnie</h1>')