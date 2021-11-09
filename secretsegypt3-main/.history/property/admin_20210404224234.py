from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

from .models import property,place ,category,properImages

# Register your models here.
class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(property ,SomeModelAdmin )
admin.site.register(category  )
admin.site.register(place  )
admin.site.register(properImages  )

