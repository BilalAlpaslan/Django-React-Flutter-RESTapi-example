from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ("name","author","created_date") #ekranda görülecek özellikler
    search_fields = ("name",) #arama yapılabilinecek özellikler
    list_fields = ("created_date") #listelenebilecek özellik
    class Meta:
        model : Article

