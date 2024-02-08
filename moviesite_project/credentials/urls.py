from django.urls import path

from credentials import views
app_name='credentials'



urlpatterns = [
    path('',views.register,name="register"),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('cbvdetail/<int:pk>/',views.UserDetailView.as_view(),name='cbvdetail'),
    path('cbvedit/<int:pk>/',views.UserEditView.as_view(),name='cbvedit'),

]
