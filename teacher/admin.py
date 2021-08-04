from django.contrib import admin
from . import models


admin.site.register(models.AddressInfo)
admin.site.register(models.EducationInfo)
admin.site.register(models.TrainingInfo)
admin.site.register(models.JobInfo)
admin.site.register(models.ExperienceInfo)


@admin.register(models.PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'photo', 'date_of_birth', 'gender', 'phone_no', 'religion', 'nationality']

# admin.site.register(models.PersonalInfo)
