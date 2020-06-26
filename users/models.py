from django.db import models
from django.contrib.auth.models import User
#resize image
from PIL import Image
from django.core.validators import RegexValidator
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    first_name = models.CharField(max_length=50, blank="True")
    last_name = models.CharField(max_length=50, blank="True")
    phone_regex = RegexValidator(regex = r'^[9876]\d{9}$', 
        message = "Enter valid phone number. Ensure 10 digit number starting with 9, 8, 7, or 6")
    phone_number = models.CharField(validators = [phone_regex], max_length=10, blank='True')
    

    def __str__(self):
        return f'{self.user.username} Profile'

    #resize image 
    def save(self, *args, **kwargs):
    	super(Profile, self).save(*args, **kwargs)

    	img = Image.open(self.image.path)

    	if img.height>300 or img.width>300:
    		output_size = (300, 300)
    		img.thumbnail(output_size)
    		img.save(self.image.path)


class Profile_Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Branch_CHOICES=[('CS','CS'),('Mech','Mech'),('ENTC','ENTC'),('IT','IT'),
    ('CHEM','CHEM'),('ETX','ETX'),('Civil','Civil'),('FY','FY')]
    branch=models.CharField(max_length=100,choices=Branch_CHOICES,default='CS')
    Year_CHOICES=[('FY','I'),('SY','II'),('TY','III'),('BE','IV')]
    academic_year=models.CharField(max_length=100,choices=Year_CHOICES,default='I')
    batch_regex = RegexValidator(regex = r'^[ABCD][1-5][1-5]$', 
        message = "example A14")
    batch = models.CharField(validators = [batch_regex], max_length=3, blank='True')
    roll_no_regex = RegexValidator(regex = r'^\d{2}$', 
        message = "example 70")
    roll_no = models.CharField(validators = [roll_no_regex], max_length=3, blank='True')
    
    def __str__(self):
        return f'{self.user.username} Profile Student'

class Profile_Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Branch_CHOICES=[('CS','CS'),('Mech','Mech'),('ENTC','ENTC'),('IT','IT'),
    ('CHEM','CHEM'),('ETX','ETX'),('Civil','Civil'),('FY','FY')]
    branch=models.CharField(max_length=100,choices=Branch_CHOICES,default='CS')
    post_of_teacher = models.CharField(max_length=100,blank='True')

    def __str__(self):
        return f'{self.user.username} Profile Teacher'





        