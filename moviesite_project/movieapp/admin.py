from django.contrib import admin

from movieapp.models import Category,Movies


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category,CategoryAdmin)

class MoviesAdmin(admin.ModelAdmin):
    list_display = ['title','rls_date','username_added','category']
    prepopulated_fields = {'slug':('title',)}
    list_per_page = 20

admin.site.register(Movies,MoviesAdmin)

