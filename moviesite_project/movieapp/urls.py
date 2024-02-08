from django.urls import path
from movieapp import views
app_name ='movieapp'

urlpatterns = [
    path('', views.AllProdCat,name="AllProdCat"),
    # path('add/',views.add_movie,name="add_movie"),
    # path('update/<int:movie_id>/',views.update,name="update"),
    path('add/',views.MovieCreateView.as_view(),name="add_movie"),
    path('feedback/',views.feedback,name="feedback"),
    path('delete/<int:movie_id>/',views.delete,name="delete"),
    path('cbvupdate/<int:pk>/',views.MovieUpdateView.as_view(),name='cbvupdate'),
    path('<slug:c_slug>/',views.AllProdCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:movie_slug>/',views.MovieDetails,name='MovieCatDetail'),

]

