from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView,CreateView
from movieapp.forms import MovieForm
from movieapp.models import Category,Movies
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.
class MovieUpdateView(UpdateView):
    model=Movies
    template_name = 'update.html'
    # context_object_name = 'movie'
    fields=['title','image','description','rls_date','actors','category','yt_link','username_added']
    success_url = reverse_lazy('movieapp:AllProdCat')

class MovieCreateView(CreateView):
    model=Movies
    template_name = 'create.html'
    fields = ['title','image', 'description', 'rls_date', 'actors', 'category', 'yt_link', 'username_added']
    success_url = reverse_lazy('movieapp:AllProdCat')

def AllProdCat(request,c_slug=None):
    c_page=None
    movies_list=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        movies_list=Movies.objects.all().filter(category=c_page)
    else:
        movies_list=Movies.objects.all()
    paginator=Paginator(movies_list,6)
    try:
        page=int(request.GET.get('page',1))
    except:
        page=1
    try:
        movies=paginator.page(page)
    except (EmptyPage,InvalidPage):
        movies=paginator.page(paginator.num_pages)

    return render(request,"home.html",{'category':c_page,'movies':movies})


def MovieDetails(request,c_slug,movie_slug):
    try:
        movie=Movies.objects.get(category__slug=c_slug,slug=movie_slug)
    except Exception as e:
        raise e
    return render(request,"movie.html",{'movie':movie})

# def add_movie(request):
#     if request.method=='POST':
#         mname=request.POST['name']
#         mimg = request.FILES['img']
#         mdesc = request.POST['desc']
#         mdate = request.POST['date']
#         mactors = request.POST['act']
#         mcategory = request.POST['cat']
#         mlink = request.POST['link']
#
#         movie=Movies.objects.create(title=mname,image=mimg,description=mdesc,rls_date=mdate,actors=mactors,category=mcategory,yt_link=mlink)
#         movie.save()
#         return redirect('/')
#     return render(request,"add.html")

# def update(request,movie_id):
#     movie=Movies.objects.get(id=movie_id)
#     form=MovieForm(request.POST or None,request.FILES,instance=movie)
#     if form.is_valid():
#         form.save()
#         return redirect('/')
#     return render(request,"update.html",{'m_movie':movie,'m_form':form})


def delete(request,movie_id):
        if request.method=='POST':
            movie=Movies.objects.get(id=movie_id)
            movie.delete()
            return redirect('movieapp:AllProdCat')
        return render(request,"delete.html")

def feedback(request):
    return render(request,"feedback.html")
