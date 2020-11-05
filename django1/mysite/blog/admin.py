from django.contrib import admin
from .models import Author,Catagory,Articles



class AuthorModel(admin.ModelAdmin):
    list_display = ['__str__']
    search_fields = ['__str__', 'details']

    class Meta:
        Model = Author
admin.site.register (Author, AuthorModel)

class ArticlesModel(admin.ModelAdmin):
    list_display = ['__str__', 'posted']
    search_fields = ['__str__', 'details']
    list_filter = ['posted',]
    list_per_page = 10

    class Meta:
        Model = Articles

admin.site.register (Articles, ArticlesModel)

class CatagoryModel(admin.ModelAdmin):
    list_display = ['__str__',]
    search_fields = ['__str__',]
    list_per_page = 10

    class Meta:
        Model = Catagory
admin.site.register (Catagory, CatagoryModel)