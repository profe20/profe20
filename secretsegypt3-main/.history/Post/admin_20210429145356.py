from django.contrib import admin
from .models import Post,category

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_filter = ['active' ,'created']
    list_display = ['title' , 'created', 'active']
    search_fields = ['title', 'content' ]
 



admin.site.register(category  )
admin.site.register(Post , PostAdmin)
