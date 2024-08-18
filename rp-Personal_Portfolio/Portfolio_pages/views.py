from django.shortcuts import render

def home(request):
    return render(request, 'Portfolio_pages/home.html', {})