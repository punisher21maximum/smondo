from django.db import models
from django.contrib.auth.models import User
#resize image
from PIL import Image
from django.core.validators import RegexValidator

#regex validators
phone_regex = RegexValidator(regex = r'^[9876]\d{9}$', 
    message = "Required 10 digits. Starting with 9,8,7, or 6")
#func validators
 

#CHOICES
society_CHOICES = [('Smondo 3.0', 'Smondo 3.0'), ('Other', 'Other')]
b=list('ABCDEFGHI')
bldg_CHOICES = list(zip(b,b))
fl = list(range(1,15))
fl = [str(i) for i in fl]
floor_CHOICES = list(zip(fl,fl))
ft = list('1234')
flat_CHOICES = list(zip(ft,ft))

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #personal info
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    first_name = models.CharField(max_length=50, blank="True")
    last_name = models.CharField(max_length=50, blank="True")
    #contact details
    phone_number = models.CharField(validators = [phone_regex], max_length=10, 
    blank='True', help_text='10 digit. start with 9,8,7 or 6')
    #address
    society = models.CharField(max_length=50, choices=society_CHOICES, 
    default='Smondo 3.0')
    bldg = models.CharField(max_length=50, choices=bldg_CHOICES, default='A')
    floor = models.CharField(choices=floor_CHOICES , blank=True, max_length=10,
    default=1)
    flat_no = models.CharField(choices=flat_CHOICES , blank=True, max_length=10,
    default=1)
     
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



# class Profile_Student(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     Branch_CHOICES=[('CS','CS'),('Mech','Mech'),('ENTC','ENTC'),('IT','IT'),
#     ('CHEM','CHEM'),('ETX','ETX'),('Civil','Civil'),('FY','FY')]
#     branch=models.CharField(max_length=100,choices=Branch_CHOICES,default='CS')
#     Year_CHOICES=[('FY','I'),('SY','II'),('TY','III'),('BE','IV')]
#     academic_year=models.CharField(max_length=100,choices=Year_CHOICES,default='I')
#     batch_regex = RegexValidator(regex = r'^[ABCD][1-5][1-5]$', 
#         message = "example A14")
#     batch = models.CharField(validators = [batch_regex], max_length=3, blank='True')
#     roll_no_regex = RegexValidator(regex = r'^\d{2}$', 
#         message = "example 70")
#     roll_no = models.CharField(validators = [roll_no_regex], max_length=3, blank='True')
    
#     def __str__(self):
#         return f'{self.user.username} Profile Student'

# class Profile_Teacher(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     Branch_CHOICES=[('CS','CS'),('Mech','Mech'),('ENTC','ENTC'),('IT','IT'),
#     ('CHEM','CHEM'),('ETX','ETX'),('Civil','Civil'),('FY','FY')]
#     branch=models.CharField(max_length=100,choices=Branch_CHOICES,default='CS')
#     post_of_teacher = models.CharField(max_length=100,blank='True')

#     def __str__(self):
#         return f'{self.user.username} Profile Teacher'





        