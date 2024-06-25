from django.db import models

class Client(models.Model):
    fullname = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=13, unique=True)


    def __str__(self) -> str:
        return self.fullname



class House(models.Model):
    name =  models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True, null=True)
    latitude = models.CharField(max_length=200,blank=True, null=True)
    longitude  = models.CharField(max_length=200,blank=True, null=True)
    image_data1 = models.ImageField(upload_to="home",blank=True, null=True)
    image_data2 = models.ImageField(upload_to="home",blank=True, null=True)
    image_data3 = models.ImageField(upload_to="home",blank=True, null=True)
    image_data4 = models.ImageField(upload_to="home",blank=True, null=True)
    image_data5 = models.ImageField(upload_to="home",blank=True, null=True)

    def __str__(self) -> str:
        return self.name     