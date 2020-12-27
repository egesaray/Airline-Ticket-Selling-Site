from django.contrib import admin

# Register your models here.

from .models import *

# *******************************************eski***********
# admin.site.register(user)
# admin.site.register(ticket)
# admin.site.register(Order)
# *******************************************eski***********



admin.site.register(CreditCard)
admin.site.register(Feedback)
admin.site.register(Ticket)
admin.site.register(ChildTicket)
admin.site.register(Flight)
admin.site.register(Airport)
admin.site.register(Ticket_Flight)
admin.site.register(Airport_Flight)






# *******************************************eski***********
# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('commenter', 'comment_content', 'product', 'created_on', 'active')
#     list_filter = ('active', 'created_on')
#     search_fields = ('commenter', 'comment_content')
#     actions = ['approve_comments']
#
#     def approve_comments(self, request, queryset):
#         queryset.update(active=True)
# *******************************************eski***********
