from django.contrib import admin

from .models import *

# Register your models here.


@admin.register(AcademicInfo)
class AcademicInfoAdmin(admin.ModelAdmin):
    list_display = ['personal_info', 'class_info', 'registration_no', 'status', 'date']
    # admin.site.register(AcademicInfo)


@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'photo', 'date_of_birth', 'gender', 'phone_no', 'religion', 'nationality']
    # admin.site.register(PersonalInfo)


@admin.register(StudentAddressInfo)
class StudentAddressInfoAdmin(admin.ModelAdmin):
    list_display = ['district', 'upazilla', 'union', 'village']
    # admin.site.register(StudentAddressInfo)


admin.site.register(GuardianInfo)
admin.site.register(EmergencyContactDetails)
admin.site.register(PreviousAcademicInfo)
admin.site.register(PreviousAcademicCertificate)


@admin.register(EnrolledStudent)
class EnrolledStudentAdmin(admin.ModelAdmin):
    list_display = ['class_name', 'student', 'roll', 'date']
# admin.site.register(EnrolledStudent)
