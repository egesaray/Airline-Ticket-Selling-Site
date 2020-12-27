from django.contrib import admin

# Register your models here.
from .models import *
from .models import *

admin.site.register(user)
admin.site.register(ticket)
admin.site.register(Order)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('commenter', 'comment_content', 'product', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('commenter', 'comment_content')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)