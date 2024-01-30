from django.contrib import admin
from .models import *

class Campaign_data(admin.ModelAdmin):
    list_display = ('id', 'subject', 'preview_text','article_url','html_content','updated_at')
    search_fields = ('subject',)

class Subscriber_data(admin.ModelAdmin):
    list_display = ('id', 'email','first_name')
    search_fields = ('first_name','email')
    
admin.site.register(Subscriber,Subscriber_data)
admin.site.register(Campaign,Campaign_data)
