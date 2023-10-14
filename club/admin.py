from django.contrib import admin
from .models import List_Opps, Category, List_Opps_course, List_Opps_des, List_Opps_others, List_Opps_volon, List_Opps_program, List_Opps_intern,Training, User

# Register your models here.

admin.site.register(List_Opps)
admin.site.register(Category)
admin.site.register(List_Opps_course)
admin.site.register(List_Opps_des)
admin.site.register(List_Opps_others)
admin.site.register(List_Opps_intern)
admin.site.register(List_Opps_volon)
admin.site.register(List_Opps_program)
admin.site.register(Training)
admin.site.register(User)
