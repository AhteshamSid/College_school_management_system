from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(EmployeeAddressInfo)
admin.site.register(EducationInfo)
admin.site.register(TrainingInfo)
admin.site.register(EmployeeJobInfo)
admin.site.register(ExperienceInfo)


@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'photo', 'date_of_birth', 'gender', 'phone_no', 'religion', 'nationality']

# admin.site.register(PersonalInfo)
