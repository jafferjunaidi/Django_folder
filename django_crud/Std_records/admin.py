from django.contrib import admin
from .models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=('std_name','std_age','std_city','std_mail') # to show columns in database
admin.site.register(Student,StudentAdmin)