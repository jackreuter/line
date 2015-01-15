from django.contrib import admin

from .models import Link
from .forms import LinkCreationForm

class LinkAdmin(admin.ModelAdmin):
    add_form = LinkCreationForm

    date_heirarchy = 'created_at'
    fields = ('title', 'url', 'posted_by')
    list_display = ['title', 'url', 'created_at', 'updated_at', 'posted_by']
    list_filter = ['posted_by']
    search_fields = ['title', 'url']
    
admin.site.register(Link, LinkAdmin)
