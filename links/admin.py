from django.contrib import admin

from .models import Link

class LinkAdmin(admin.ModelAdmin):
    date_heirarchy = 'created_at'
    fields = ('title', 'content', 'posted_by')
    list_display = ['title', 'created_at', 'updated_at', 'posted_by']
    list_filter = ['posted_by']
    search_fields = ['title', 'content']
    
admin.site.register(Link, LinkAdmin)
