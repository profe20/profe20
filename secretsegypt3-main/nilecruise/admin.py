from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import nilecruise,category,place,nilecruiseImages,cnilecruiseBook

# Register your models here.

# Register your models here.

class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(nilecruise ,SomeModelAdmin )
admin.site.register(category  )
admin.site.register(place  )
admin.site.register(nilecruiseImages  )
admin.site.register(cnilecruiseBook  )
