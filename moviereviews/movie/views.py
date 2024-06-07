from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    searchTerm = request.GET.get('searchMovie')
    return  render(request, 'home.html', {'name':'Ola',
                                          'searchTerm': searchTerm})

def about(request):
    return HttpResponse('<h1>Strona o mnie</h1>')

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', { 'email': email})