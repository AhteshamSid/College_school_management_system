import random

from django.db import models
from academic.models import Department
from administration.models import Designation
from address.models import District, Upazilla, Union


class AddressInfo(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    upazilla = models.ForeignKey(Upazilla, on_delete=models.CASCADE)
    union = models.ForeignKey(Union, on_delete=models.CASCADE)
    village = models.TextField(blank=True)

    def __str__(self):
        return self.village

class EducationInfo(models.Model):
    name_of_exam = models.CharField(max_length=100, blank=True)
    institute = models.CharField(max_length=255, blank=True)
    group = models.CharField(max_length=100, blank=True)
    grade = models.CharField(max_length=45, blank=True)
    board = models.CharField(max_length=45, blank=True)
    passing_year = models.IntegerField(default=2000+random.randint(00, 11), )

    def __str__(self):
        return self.name_of_exam

class TrainingInfo(models.Model):
    training_name = models.CharField(max_length=100, blank=True)
    year = models.IntegerField(default=2000+random.randint(00, 11))
    duration = models.IntegerField(default=random.randint(00, 11))
    place = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.training_name

class JobInfo(models.Model):
    category_choice = (
        ('bcs', 'BCS'),
        ('nationalized', 'Nationalized'),
        ('10% quota', '10% quota'),
        ('non govt.', 'Non Govt.')
    )
    category = models.CharField(choices=category_choice, max_length=45, blank=True)
    joning_date = models.DateField(default="2018-5-5")
    institute_name = models.CharField(max_length=100, blank=True)
    job_designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    scale = models.IntegerField(default=random.randint(0, 9))
    grade_of_post = models.CharField(max_length=45, blank=True)
    first_time_scale_due_year = models.IntegerField(default=2000+random.randint(00, 11))
    second_time_scale_due_year = models.IntegerField(default=2010+random.randint(00, 11))
    promotion_due_year = models.IntegerField(default=2005+random.randint(00, 11))
    recreation_leave_due_year = models.IntegerField(default=2010+random.randint(00, 11))
    expected_retirement_year = models.IntegerField(default=2040+random.randint(00, 11))

    def __str__(self):
        return self.institute_name

class ExperienceInfo(models.Model):
    institute_name = models.CharField(max_length=100, blank=True)
    designation = models.CharField(max_length=45, blank=True)
    trainer = models.CharField(max_length=45, blank=True)

    def __str__(self):
        return self.institute_name

class PersonalInfo(models.Model):
    name = models.CharField(max_length=45)
    photo = models.ImageField()
    date_of_birth = models.DateField(default="2018-5-5")
    place_of_birth = models.CharField(max_length=45, blank=True)
    nationality_choice = (
        ('India', 'India'),
        ('Others', 'Others')
    )
    nationality = models.CharField(max_length=45, choices=nationality_choice, blank=True)
    religion_choice = (
        ('Islam', 'Islam'),
        ('Hinduism', 'Hinduism'),
        ('Buddhism', 'Buddhism'),
        ('Christianity', 'Christianity'),
        ('Others', 'Others')
    )
    religion = models.CharField(max_length=45, choices=religion_choice, blank=True)
    gender_choice = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    )
    gender = models.CharField(choices=gender_choice, max_length=10, blank=True)
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
    e_tin = models.IntegerField(unique=True, default=random.randint(0000000000, 9999999999))
    nid = models.IntegerField(unique=True, default=random.randint(0000000000, 9999999999))
    driving_license_passport = models.IntegerField(unique=True, default=random.randint(00000000, 99999999))
    phone_no = models.CharField(max_length=11, unique=True, default=random.randint(00000000, 99999999))
    email = models.CharField(max_length=255, default="example@gmail.com")
    father_name = models.CharField(max_length=45, blank=True)
    mother_name = models.CharField(max_length=45, blank=True)
    marital_status_choice = (
        ('married', 'Married'),
        ('widowed', 'Widowed'),
        ('separated', 'Separated'),
        ('divorced', 'Divorced'),
        ('single', 'Single')
    )
    marital_status = models.CharField(choices=marital_status_choice, max_length=10, blank=True)
    address = models.ForeignKey(AddressInfo, on_delete=models.CASCADE, null=True)
    education = models.ForeignKey(EducationInfo, on_delete=models.CASCADE, null=True)
    training = models.ForeignKey(TrainingInfo, on_delete=models.CASCADE, null=True)
    job = models.ForeignKey(JobInfo, on_delete=models.CASCADE, null=True)
    experience = models.ForeignKey(ExperienceInfo, on_delete=models.CASCADE, null=True)
    is_delete = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
