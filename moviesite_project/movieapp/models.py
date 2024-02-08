from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='category',blank=True)

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def get_url(self):
        return reverse('movieapp:products_by_category', args=[self.slug])


    def __str__(self):
        return '{}'.format(self.name)

class Movies(models.Model):
    title=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    image = models.ImageField(upload_to='movie', blank=True)
    description=models.TextField(blank=True)
    rls_date = models.DateField()
    actors = models.TextField(blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    yt_link=models.URLField(max_length=250)
    username_added=models.CharField(max_length=250)
    class Meta:
        ordering=('title',)
        verbose_name='movie'
        verbose_name_plural='movies'

    def get_url(self):
        return reverse('movieapp:MovieCatDetail', args=[self.category.slug, self.slug])

    def __str__(self):
        return '{}'.format(self.title)

