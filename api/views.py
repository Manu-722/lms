
from django.shortcuts import render

def index(request):
    return render(request, 'users_index.html')
