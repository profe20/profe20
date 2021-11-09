from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

from .models import packages,place ,packages,packagesBook,category,packagesImages

# Register your models here.
class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(packages ,SomeModelAdmin )
admin.site.register(category  )
admin.site.register(place  )
admin.site.register(packagesImages  )
admin.site.register(packagesBook  )
