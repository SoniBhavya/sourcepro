from django.contrib import admin

# Register your models here.
from .models import login_details
from .models import user_details
from .models import all_course
from .models import user_courses


admin.site.register(login_details)
admin.site.register(user_details)
admin.site.register(all_course)
admin.site.register(user_courses)