from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Champs à afficher dans la liste des articles
    list_display = ('title', 'author', 'created_on', 'updated_on', 'status')
    
    # Filtres disponibles dans la sidebar
    list_filter = ('status', 'created_on', 'author')
    
    # Champs de recherche
    search_fields = ('title', 'content', 'author__username')
    
    # Pré-remplir le slug à partir du titre
    prepopulated_fields = {'slug': ('title',)}
    
    # Champs pour l'édition rapide dans la liste
    list_editable = ('status',)
    
    # Pagination
    list_per_page = 20
    
    # Configuration des champs dans le formulaire d'édition
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'author', 'content', 'image')
        }),
        ('Status', {
            'fields': ('status',),
            'classes': ('collapse',)  # Permet de masquer cette section par défaut
        }),
        ('Dates', {
            'fields': ('created_on', 'updated_on'),
            'classes': ('collapse',)  # Permet de masquer cette section par défaut
        }),
    )
    
    # Affichage des champs en lecture seule
    readonly_fields = ('created_on', 'updated_on')