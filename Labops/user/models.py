from djongo import models
# Creating  models here.
# creating user model
class Person(models.Model):
     user_name= models.CharField(max_length=20)
     email= models.EmailField(max_length=30)
     password=models.IntegerField()
     password_validation=models.IntegerField()
     sign=models.ImageField(upload_to="user/images",default="")
     profile_photo=models.ImageField(upload_to="user/images/user",default="")
#creating contracts models
class Contracts(models.Model):
    contractor_name=models.CharField(max_length=20)
    contract_desc=models.TextField(max_length=255)
    discount_type=models.CharField(max_length=20,choices=(
         ("Percentage","%age"),
         ("Custom Price","Custom Price")
    ))
    per_value=models.IntegerField()       
#creating patients models
class patient(models.Model):
    patient_name=models.CharField(max_length=20)
    nationality=models.CharField(max_length=20,default="Indian")
    national_id=models.PositiveBigIntegerField()
    p_email= models.EmailField(max_length=30)
    phone_no=models.BigIntegerField()
    Gender=models.CharField(max_length=10,choices=(
         ("Male","Male"),
         ("Female","Female")
    ))
    date_of_birth=models.DateField()
    Age=models.CharField(max_length=20,default="0")
    age_type=models.CharField(max_length=10,choices=(
         ("Year","Year"),
         ("Month","Month"),
         ("Days","Days")
    ))
    address=models.CharField(max_length=255)
    
    patient_photo=models.ImageField(upload_to="user/images/patient",default="NONE")
    def __str__(self):
         return self.patient_name

#creating invoice models
class Invoice(models.Model):
    
     created_by= models.ForeignKey(Person, on_delete=models.CASCADE)
     patient_name=models.ForeignKey(patient,on_delete=models.CASCADE)
     contract=models.ForeignKey(Contracts,on_delete=models.CASCADE)
#creating doctors models
class Doctors(models.Model):
     Doctor_name=models.CharField(max_length=20)
     doctor_email=models.EmailField(max_length=30,default="NONE")
     d_phone=models.BigIntegerField()
     commission=models.IntegerField()
     d_address=models.CharField(max_length=255)  
     def __str__(self):
         return self.Doctor_name
#creating tests models

               