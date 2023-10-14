

# users/models.py

# club/models.py

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email








class Category(models.Model):
    cate_name = models.CharField(max_length=50)
    def __str__(self):
        return self.cate_name


class List_Opps(models.Model):
    title = models.CharField(max_length=40)
    description =models.CharField(max_length=2000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category")
    url_opp = models.CharField(max_length=5000)
    time = models.CharField(max_length=50)
    card_des = models.CharField(max_length=60)
    img = models.ImageField(null=True, blank=True, upload_to="imagesopps")

    def __str__(self):
            return self.title
    

class List_Opps_course(models.Model):
    title1 = models.CharField(max_length=40)
    description1 =models.CharField(max_length=2000)
    short_des1 = models.CharField(max_length=2000)
    category1 = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category1")
    url_opp1 = models.CharField(max_length=5000)
    time1 = models.CharField(max_length=50)
    img1 = models.ImageField(null=True, blank=True, upload_to="imagesopps")


    def __str__(self):
            return self.title1
    

class List_Opps_intern(models.Model):
    title3 = models.CharField(max_length=40)
    description3 =models.CharField(max_length=2000)
    short_des3 = models.CharField(max_length=2000)
    category3 = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category3")
    url_opp3 = models.CharField(max_length=5000)
    time3 = models.CharField(max_length=50)
    img3 = models.ImageField(null=True, blank=True, upload_to="imagesopps")


    def __str__(self):
            return self.title3
    

class List_Opps_program(models.Model):
    title4 = models.CharField(max_length=40)
    description4 =models.CharField(max_length=2000)
    short_des4 = models.CharField(max_length=2000)
    category4 = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category4")
    url_opp4 = models.CharField(max_length=5000)
    time4 = models.CharField(max_length=50)
    img4 = models.ImageField(null=True, blank=True, upload_to="imagesopps")


    def __str__(self):
            return self.title4
    
class List_Opps_volon(models.Model):
    title5 = models.CharField(max_length=40)
    description5 =models.CharField(max_length=2000)
    short_des5 = models.CharField(max_length=2000)
    category5 = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category5")
    url_opp5 = models.CharField(max_length=5000)
    time5 = models.CharField(max_length=50)
    img5 = models.ImageField(null=True, blank=True, upload_to="imagesopps")


    def __str__(self):
            return self.title5
    

class List_Opps_others(models.Model):
    title6 = models.CharField(max_length=40)
    description6 =models.CharField(max_length=2000)
    short_des6 = models.CharField(max_length=2000)
    category6 = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category6")
    url_opp6 = models.CharField(max_length=5000)
    time6 = models.CharField(max_length=50)
    img6 = models.ImageField(null=True, blank=True, upload_to="imagesopps")


    def __str__(self):
            return self.title6
    

class Training(models.Model):
    title7 = models.CharField(max_length=40)
    description7 =models.CharField(max_length=2000)
    short_des7 = models.CharField(max_length=2000)
    category7 = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category7")
    url_opp7 = models.CharField(max_length=5000)
    time7 = models.CharField(max_length=50)
    img7 = models.ImageField(null=True, blank=True, upload_to="imagesopps")


    def __str__(self):
            return self.title7
    

class List_Opps_des(models.Model):
    title2 = models.CharField(max_length=40)
    description2 =models.CharField(max_length=2000)
    description2_1 =models.CharField(max_length=2000)
    description2_2 =models.CharField(max_length=2000)
    category2 = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category2")
    url_opp2 = models.CharField(max_length=5000)
    time22 = models.CharField(max_length=50)
    img2 = models.ImageField(null=True, blank=True, upload_to="imagesopps")


    def __str__(self):
            return self.title2
    



