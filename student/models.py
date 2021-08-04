from django.db import models
import random
from django.apps import apps

from academic.models import ClassInfo, ClassRegistration  #apps.get_model('academic', 'District')
from address.models import District, Upazilla, Union

class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='student-photos/')
    blood_group_choice = (
        ('a+', 'A+'),
        ('o+', 'O+'),
        ('b+', 'B+'),
        ('ab+', 'AB+'),
        ('a-', 'A-'),
        ('o-', 'O-'),
        ('b-', 'B-'),
        ('ab-', 'AB-')
    )
    blood_group = models.CharField(choices=blood_group_choice, max_length=5, blank=True)
    date_of_birth = models.DateField(default="2018-5-5", blank=True)
    gender_choice = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    )
    gender = models.CharField(choices=gender_choice, max_length=10, blank=True)
    phone_no = models.CharField(max_length=11, blank=True)
    email = models.EmailField(blank=True)
    birth_certificate_no = models.IntegerField(default=random.randint(000000, 999999))
    religion_choice = (
        ('Islam', 'Islam'),
        ('Hinduism', 'Hinduism'),
        ('Buddhism', 'Buddhism'),
        ('Christianity', 'Christianity'),
        ('Others', 'Others')
    )
    religion = models.CharField(choices=religion_choice, max_length=45, blank=True)
    nationality_choice = (
        ('India', 'India'),
        ('Others', 'Others')
    )
    nationality = models.CharField(choices=nationality_choice, max_length=45, blank=True)

    def __str__(self):
        return self.name

class StudentAddressInfo(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    upazilla = models.ForeignKey(Upazilla, on_delete=models.CASCADE)
    union = models.ForeignKey(Union, on_delete=models.CASCADE)
    village = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.village

class GuardianInfo(models.Model):
    father_name = models.CharField(max_length=100, blank=True)
    father_phone_no = models.CharField(max_length=11, blank=True)
    father_occupation_choice = (
        ('Agriculture', 'Agriculture'),
        ('Banker', 'Banker'),
        ('Business', 'Business'),
        ('Doctor', 'Doctor'),
        ('Farmer', 'Farmer'),
        ('Fisherman', 'Fisherman'),
        ('Public Service', 'Public Service'),
        ('Private Service', 'Private Service'),
        ('Shopkeeper', 'Shopkeeper'),
        ('Driver', 'Driver'),
        ('Worker', 'Worker'),
        ('N/A', 'N/A'),
    )
    father_occupation = models.CharField(choices=father_occupation_choice, max_length=45, blank=True)
    father_yearly_income = models.IntegerField( default=444444, blank=True)
    mother_name = models.CharField(max_length=100, blank=True)
    mother_phone_no = models.CharField(max_length=11, blank=True)
    mother_occupation_choice = (
        ('Agriculture', 'Agriculture'),
        ('Banker', 'Banker'),
        ('Business', 'Business'),
        ('Doctor', 'Doctor'),
        ('Farmer', 'Farmer'),
        ('Fisherman', 'Fisherman'),
        ('Public Service', 'Public Service'),
        ('Private Service', 'Private Service'),
        ('Shopkeeper', 'Shopkeeper'),
        ('Driver', 'Driver'),
        ('Worker', 'Worker'),
        ('N/A', 'N/A'),
    )
    mother_occupation = models.CharField(choices=mother_occupation_choice, max_length=45, blank=True)
    guardian_name = models.CharField(max_length=100, blank=True)
    guardian_phone_no = models.CharField(max_length=11, blank=True)
    guardian_email = models.EmailField(blank=True)
    relationship_choice = (
        ('Father', 'Father'),
        ('Mother', 'Mother'),
        ('Brother', 'Brother'),
        ('Uncle', 'Uncle'),
        ('Aunt', 'Aunt'),
    )
    relationship_with_student = models.CharField(choices=relationship_choice, max_length=45, blank=True)

    def __str__(self):
        return self.guardian_name

class EmergencyContactDetails(models.Model):
    emergency_guardian_name = models.CharField(max_length=100, blank=True)
    address = models.TextField( blank=True)
    relationship_choice = (
        ('Father', 'Father'),
        ('Mother', 'Mother'),
        ('Brother', 'Brother'),
        ('Uncle', 'Uncle'),
        ('Aunt', 'Aunt'),
    )
    relationship_with_student = models.CharField(choices=relationship_choice, max_length=45, blank=True)
    phone_no = models.CharField(max_length=11, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.emergency_guardian_name

class PreviousAcademicInfo(models.Model):
    institute_name = models.CharField(max_length=100, blank=True)
    name_of_exam = models.CharField(max_length=100, blank=True)
    group = models.CharField(max_length=45, blank=True)
    gpa = models.CharField(max_length=10, blank=True)
    board_roll = models.IntegerField(default=444444, blank=True)
    passing_year = models.IntegerField(default=2010+random.randint(00, 11))

    def __str__(self):
        return self.institute_name

class PreviousAcademicCertificate(models.Model):
    birth_certificate = models.FileField(upload_to='documents/', null=True, blank=True)
    release_letter = models.FileField(upload_to='documents/', null=True, blank=True)
    testimonial = models.FileField(upload_to='documents/', null=True, blank=True)
    marksheet = models.FileField(upload_to='documents/', null=True, blank=True)
    stipen_certificate = models.FileField(upload_to='documents/', null=True, blank=True)
    other_certificate = models.FileField(upload_to='documents/', null=True, blank=True)

class AcademicInfo(models.Model):
    class_info = models.ForeignKey(ClassInfo, on_delete=models.CASCADE)
    registration_no = models.IntegerField(unique=True, default=random.randint(000000, 999999))
    status_select = (
        ('not enroll', 'Not Enroll'),
        ('enrolled', 'Enrolled'),
        ('regular', 'Regular'),
        ('irregular', 'Irregular'),
        ('passed', 'Passed'),
    )
    status = models.CharField(choices=status_select, default='not enroll', max_length=15)
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, null=True)
    address_info = models.ForeignKey(StudentAddressInfo, on_delete=models.CASCADE, blank=True)
    guardian_info = models.ForeignKey(GuardianInfo, on_delete=models.CASCADE, null=True)
    emergency_contact_info = models.ForeignKey(EmergencyContactDetails, on_delete=models.CASCADE, null=True)
    previous_academic_info = models.ForeignKey(PreviousAcademicInfo, on_delete=models.CASCADE, null=True)
    previous_academic_certificate = models.ForeignKey(PreviousAcademicCertificate, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return str(self.registration_no)

class EnrolledStudent(models.Model):
    class_name = models.ForeignKey(ClassRegistration, on_delete=models.CASCADE)
    student = models.OneToOneField(AcademicInfo, on_delete=models.CASCADE)
    roll = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ['class_name', 'roll']
    
    def __str__(self):
        return str(self.roll)

