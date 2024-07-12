from django.db import models


class Client(models.Model):
    fullname = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=13, unique=True)
    username =  models.CharField(max_length=200, blank=True, null=True)

    def __str__(self) -> str:
        return self.fullname


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Subcategory(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(blank=True, null=True, upload_to="subcategory/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    


class House(models.Model):
    name =  models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True, null=True)
    latitude = models.CharField(max_length=200,blank=True, null=True)
    longitude  = models.CharField(max_length=200,blank=True, null=True)
    image_data1 = models.ImageField(upload_to="home",blank=True, null=True)
    discount = models.PositiveBigIntegerField(default=0,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    category=models.ForeignKey(Category, on_delete=models.CASCADE,blank=True, null=True )
    price = models.PositiveBigIntegerField(default=0,blank=True, null=True)


    def __str__(self):
        return self.name
    