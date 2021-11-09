from django.contrib import admin
from .models import Post,category,slideImages,Comment

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_filter = ['active' ,'created']
    list_display = ['title' , 'created', 'active']
    search_fields = ['title', 'content' ]


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body',  'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

def approve_comments(self, request, queryset):
        queryset.update(active=True)



admin.site.register(category  )
admin.site.register(slideImages  )
admin.site.register(Post , PostAdmin)
admin.site.register(Comment , CommentAdmin)
