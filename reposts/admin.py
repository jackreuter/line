from django.contrib import admin

from .models import Repost

class RepostAdmin(admin.ModelAdmin):
    date_heirarchy = 'created_at'
    fields = ('title', 'posted_by')
    list_display = ['title', 'created_at', 'updated_at', 'posted_by']
    list_filter = ['posted_by']
    search_fields = ['title', 'url']
    
admin.site.register(Repost, RepostAdmin)

