from django import forms

from movieapp.models import Movies


class MovieForm(forms.ModelForm):
    class Meta:
        model=Movies
        fields=['title','image','description','rls_date','actors','category','yt_link','username_added']

