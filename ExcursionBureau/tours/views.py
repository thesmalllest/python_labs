from django.shortcuts import render, get_object_or_404
from .models import Tour

def home(request):
    tours = Tour.objects.all()
    return render(request, 'tours/home.html', {'tours': tours})

def tour_detail(request, pk):
    tour = get_object_or_404(Tour, pk=pk)
    return render(request, 'tours/tour_detail.html', {'tour': tour})


