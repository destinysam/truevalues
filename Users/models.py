from django.db import models

# Create your models here.
class UserModel(models.Model):
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    company_name=models.CharField(max_length=150)
    age = models.IntegerField()
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    pincode = models.IntegerField()
    email = models.EmailField()
    web = models.CharField(max_length=250)


    def __str__(self):
        
        """Method to customize the string representation """

        return self.first_name + " " + self.last_name