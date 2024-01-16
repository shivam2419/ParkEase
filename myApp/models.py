from django.db import models

# Create your models here.

class Register(models.Model):
    owner_name=models.CharField(max_length=200)
    vehicle_number=models.CharField(max_length=200)
    pnum=models.IntegerField()
    parking_id=models.CharField(max_length=200)


class signUp(models.Model):
    id = models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=200)
    pswrd=models.IntegerField()
    user_email=models.CharField(max_length=200)
    phone_num=models.IntegerField()
    adhaar_image=models.ImageField(upload_to='activity/images',default="")