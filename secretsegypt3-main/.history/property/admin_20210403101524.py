from django.contrib import admin

# Register your models here.

from .models import property,place ,category

# Register your models here.



admin.site.register(category  )
admin.site.register(place  )
admin.site.register(property  )
admin.site.register(properImages  )

