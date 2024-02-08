from django.shortcuts import render
from movieapp.models import Movies
from django.db.models import Q

# Create your views here.

def SearchResult(request):
    movies=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        movies=Movies.objects.all().filter(Q(title__contains=query) | Q(description__contains=query))
        return render(request,'search.html',{'query':query,'movies':movies})



