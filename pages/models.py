from django.db import models

# Create your models here.
class Product(models.Model):
    image1 = models.ImageField(upload_to='photos/%y/%m/%d')
    image2 = models.ImageField(upload_to='photos/%y/%m/%d')
    description = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    active = models.BooleanField(default = True)

    def __str__(self):
        return self.description
    
class Delivery(models.Model):
    FirstName = models.CharField(max_length=50, null=True,blank=True)
    LastName = models.CharField(max_length=50, null=True,blank=True)
    PhoneNumber = models.DecimalField(max_digits=11,decimal_places=0, null=True,blank=True)
    YourAddress = models.CharField(max_length= 50, null=True,blank=True)
    items = models.CharField(max_length= 50, null=True,blank=True)
    quantity = models.IntegerField(null=True,blank=False)
    size = models.CharField(max_length= 50, null=True,blank=True)
    details = models.CharField(max_length= 50, null=True,blank=True)
    
    def __str__(self):
        return self.FirstName

