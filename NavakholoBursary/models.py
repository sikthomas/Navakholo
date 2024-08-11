from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_finance = models.BooleanField(default=False)
    parent_type=models.BooleanField(default=False)
    personal_information=models.BooleanField(default=False)
    institution_information=models.BooleanField(default=False)
    parent_information=models.BooleanField(default=False)
    additional_information=models.BooleanField(default=False)
    verification_stutus=models.BooleanField(default=False)
    allocation_stutus=models.BooleanField(default=False)
    idnumber=models.IntegerField(unique=True)

    REQUIRED_FIELDS = ['email', 'idnumber']

class Usertype(models.Model):
    userid = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    role = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.userid.username} - {self.role}"

   
class PersonalInformation(models.Model):
    userid= models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    phone_number = models.PositiveIntegerField()
    ward = models.CharField(max_length=30)
    village = models.CharField(max_length=30)
    filled_date=models.DateTimeField(auto_now_add=True)
    applicand_id=models.FileField(upload_to='mediafiles',blank=True,null=True)
   
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
    admission_letter=models.FileField(upload_to='mediafiles',blank=True,null=True)
    fee_statement=models.FileField(upload_to='mediafiles',blank=True,null=True)

class ParentType(models.Model):
    user_id=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    bother_parent=models.BooleanField(default=False)
    father=models.BooleanField(default=False)
    mother=models.BooleanField(default=False)
    guardian=models.BooleanField(default=False)

class BotheParent(models.Model):
    applicant_id = models.OneToOneField(PersonalInformation, on_delete=models.CASCADE)
    father_firstname=models.CharField(max_length=50)
    father_lastname=models.CharField(max_length=50)
    father_id_no=models.CharField(max_length=50)
    father_phone_number=models.CharField(max_length=50)
    father_occupation=models.CharField(max_length=50)
    father_employer=models.CharField(max_length=50)
    father_annual_income=models.CharField(max_length=50)
    father_id=models.FileField(upload_to='mediafiles',blank=True,null=True)
    
    mother_firstname=models.CharField(max_length=50)
    mother_lastname=models.CharField(max_length=50)
    mother_id_no=models.CharField(max_length=50)
    mother_phone_number=models.CharField(max_length=50)
    mother_occupation=models.CharField(max_length=50)
    mother_employer=models.CharField(max_length=50)
    mother_annual_income=models.CharField(max_length=50)
    filled_date=models.DateTimeField(auto_now_add=True)
    mother_id=models.FileField(upload_to='mediafiles',blank=True,null=True)

class Mother(models.Model):
    applicant_id = models.OneToOneField(PersonalInformation, on_delete=models.CASCADE)
    mother_firstname=models.CharField(max_length=50)
    mother_lastname=models.CharField(max_length=50)
    mother_id_no=models.CharField(max_length=50)
    mother_phone_number=models.CharField(max_length=50)
    mother_occupation=models.CharField(max_length=50)
    mother_employer=models.CharField(max_length=50)
    mother_annual_income=models.CharField(max_length=50)
    filled_date=models.DateTimeField(auto_now_add=True)
    mother_id=models.FileField(upload_to='mediafiles',blank=True,null=True)
  

class Father(models.Model):
    applicant_id = models.OneToOneField(PersonalInformation, on_delete=models.CASCADE)
    father_firstname=models.CharField(max_length=50)
    father_lastname=models.CharField(max_length=50)
    father_id_no=models.CharField(max_length=50)
    father_phone_number=models.CharField(max_length=50)
    father_occupation=models.CharField(max_length=50)
    father_employer=models.CharField(max_length=50)
    father_annual_income=models.CharField(max_length=50)
    filled_date=models.DateTimeField(auto_now_add=True)
    father_id=models.FileField(upload_to='mediafiles',blank=True,null=True)

class Guardian(models.Model):
    applicant_id = models.OneToOneField(PersonalInformation, on_delete=models.CASCADE)
    guardian_firstname=models.CharField(max_length=50)
    guardian_lastname=models.CharField(max_length=50)
    guardian_id_no=models.CharField(max_length=50)
    guardian_phone_number=models.CharField(max_length=50)
    guardian_occupation=models.CharField(max_length=50)
    guardian_employer=models.CharField(max_length=50)
    guardian_annual_income=models.CharField(max_length=50)
    filled_date=models.DateTimeField(auto_now_add=True)
    guardian_id=models.FileField(upload_to='mediafiles',blank=True,null=True)
    father_death_certificate=models.FileField(upload_to='mediafiles',blank=True,null=True)
    mother_death_certificate=models.FileField(upload_to='mediafiles',blank=True,null=True)
   
class AdditionalInformation(models.Model):
    studentsid=models.OneToOneField(PersonalInformation, on_delete=models.CASCADE)
    number_of_siblings=models.CharField(max_length=200)
    siblings_fee=models.CharField(max_length=200)
    main_income_source=models.CharField(max_length=50)
    reason_for_applying=models.CharField(max_length=100)
    average_academic_performance=models.CharField(max_length=20)
    disability=models.CharField(max_length=20)
    disability_name=models.CharField(max_length=30)
    filled_date=models.DateTimeField(auto_now_add=True)

class Verification(models.Model):
     applicant_id= models.OneToOneField(PersonalInformation, on_delete=models.CASCADE)
     status=models.CharField(max_length=20)
     comment=models.CharField(max_length=255)
     verified_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
     verification_date=models.DateTimeField(auto_now_add=True)

class Allocation(models.Model):
     verified_id= models.OneToOneField(Verification, on_delete=models.CASCADE)
     allocated_amount=models.PositiveIntegerField()
     comment=models.CharField(max_length=100)
     allocated_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
     verification_date=models.DateTimeField(auto_now_add=True)
     