from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import *

admin.site.register(CreditCard)
admin.site.register(Feedback)
#admin.site.register(Ticketclass)
admin.site.register(Ticket)
admin.site.register(Flight)
admin.site.register(Airport)
admin.site.register(RegisteredUser)
admin.site.register(user_type)
admin.site.register(seat)

#
# admin.site.register(user)
# admin.site.register(ticket)
# admin.site.register(Order)
#
# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('commenter', 'comment_content', 'product', 'created_on', 'active')
#     list_filter = ('active', 'created_on')
#     search_fields = ('commenter', 'comment_content')
#     actions = ['approve_comments']
#
#     def approve_comments(self, request, queryset):
#         queryset.update(active=True)