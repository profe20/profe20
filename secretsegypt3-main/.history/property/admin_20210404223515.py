from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import SomeModel
# Register your models here.

from .models import property,place ,category,properImages

# Register your models here.



admin.site.register(category  )
admin.site.register(place  )
admin.site.register(property  )
admin.site.register(properImages  )

