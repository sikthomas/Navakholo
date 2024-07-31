from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_finance = models.BooleanField(default=False)
    personal_information=models.BooleanField(default=False)
    institution_information=models.BooleanField(default=False)
    parent_information=models.BooleanField(default=False)
    additional_information=models.BooleanField(default=False)
    verification_stutus=models.BooleanField(default=False)
    allocation_stutus=models.BooleanField(default=False)

class PersonalInformation(models.Model):
    userid= models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    id_number = models.PositiveIntegerField()
    phone_number = models.PositiveIntegerField()
    ward = models.CharField(max_length=30)
    village = models.CharField(max_length=30)
    filled_date=models.DateTimeField(auto_now_add=True)
   
class InstitutionalInformation(models.Model):
    application = models.OneToOneField(PersonalInformation, on_delete=models.CASCADE)
    institution_category = models.CharField(max_length=30)
    institution_name = models.CharField(max_length=50)
    admission_no = models.CharField(max_length=20)
    course = models.CharField(max_length=50)
    mode_of_study = models.CharField(max_length=30)
    year_of_study = models.PositiveIntegerField()
    course_duration = models.PositiveIntegerField()
    year_of_completion = models.DateField()
    filled_date=models.DateTimeField(auto_now_add=True)

class BotheParent(models.Model):
    applicant_id = models.OneToOneField(InstitutionalInformation, on_delete=models.CASCADE)
    father_firstname=models.CharField(max_length=50)
    father_lastname=models.CharField(max_length=50)
    father_id_no=models.CharField(max_length=50)
    father_phone_number=models.CharField(max_length=50)
    father_occupation=models.CharField(max_length=50)
    father_employer=models.CharField(max_length=50)
    father_annual_income=models.CharField(max_length=50)
    
    mother_firstname=models.CharField(max_length=50)
    mother_firstname_lastname=models.CharField(max_length=50)
    mother_id_no=models.CharField(max_length=50)
    mother_phone_number=models.CharField(max_length=50)
    mother_occupation=models.CharField(max_length=50)
    mother_employer=models.CharField(max_length=50)
    mother_annual_income=models.CharField(max_length=50)
    filled_date=models.DateTimeField(auto_now_add=True)
    

class Mother(models.Model):
    applicantid = models.OneToOneField(InstitutionalInformation, on_delete=models.CASCADE)
    mother_firstname=models.CharField(max_length=50)
    mother_firstname_lastname=models.CharField(max_length=50)
    mother_id_no=models.CharField(max_length=50)
    mother_phone_number=models.CharField(max_length=50)
    mother_occupation=models.CharField(max_length=50)
    mother_employer=models.CharField(max_length=50)
    mother_annual_income=models.CharField(max_length=50)
    filled_date=models.DateTimeField(auto_now_add=True)
  

class Father(models.Model):
    applicantId = models.OneToOneField(InstitutionalInformation, on_delete=models.CASCADE)
    father_firstname=models.CharField(max_length=50)
    father_lastname=models.CharField(max_length=50)
    father_id_no=models.CharField(max_length=50)
    father_phone_number=models.CharField(max_length=50)
    father_occupation=models.CharField(max_length=50)
    father_employer=models.CharField(max_length=50)
    father_annual_income=models.CharField(max_length=50)
    filled_date=models.DateTimeField(auto_now_add=True)

class Guardian(models.Model):
    applicantID = models.OneToOneField(InstitutionalInformation, on_delete=models.CASCADE)
    guardian_firstname=models.CharField(max_length=50)
    guardian_lastname=models.CharField(max_length=50)
    guardian_id_no=models.CharField(max_length=50)
    guardian_phone_number=models.CharField(max_length=50)
    guardian_occupation=models.CharField(max_length=50)
    guardian_employer=models.CharField(max_length=50)
    guardian_annual_income=models.CharField(max_length=50)
    filled_date=models.DateTimeField(auto_now_add=True)
   
class AdditionalInformation(models.Model):
    studentsid=models.OneToOneField(PersonalInformation, on_delete=models.CASCADE)
    number_of_siblings=models.CharField(max_length=200)
    main_income_source=models.CharField(max_length=50)
    reason_for_applying=models.CharField(max_length=100)
    average_academic_performance=models.CharField(max_length=20)
    disability=models.CharField(max_length=20)
    disability_name=models.CharField(max_length=30)
    filled_date=models.DateTimeField(auto_now_add=True)







    
    
   