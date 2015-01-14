from django.contrib import admin

from .models import Link

class LinkAdmin(admin.ModelAdmin):
    date_heirarchy = 'created_at'
    fields = ('title', 'url', 'posted_by')
    list_display = ['title', 'url', 'created_at', 'updated_at', 'posted_by']
    list_filter = ['posted_by']
    search_fields = ['title', 'url']
    
admin.site.register(Link, LinkAdmin)
