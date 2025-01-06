from django.shortcuts import render
from .models import Jobs

# Create your views here.
def home(request):
    jobs = Jobs.objects.all()
    return render(request, 'home.html', {'jobs': jobs})