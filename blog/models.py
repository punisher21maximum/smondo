from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms
lenn = 100

#make CHOICES from list
def func_CHOICES(k):
	k = k.split()
	return list(zip(k, k))

class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	#common fields
	title = models.CharField(max_length=100, help_text='like pulsar, duke')
	desc = models.TextField("Description")
	year = models.PositiveIntegerField("Year", blank=True, null=True, 
		help_text='bought year')
	#pricing
	sell_price = models.PositiveIntegerField(blank=True, null=True)
	rent_hour = models.PositiveIntegerField("Rent price per hour", blank=True, null=True)
	rent_day = models.PositiveIntegerField("Rent price per day", blank=True, null=True)
	rent_week = models.PositiveIntegerField("Rent price per week", blank=True, null=True)
	rent_month = models.PositiveIntegerField("Rent price per month", blank=True, null=True)
	#images
	img1 = models.ImageField("image 1", upload_to='post_images', default='default.jpg')
	img2 = models.ImageField("image 2",upload_to='post_images', default='default.jpg')
	img3 = models.ImageField("image 3",upload_to='post_images', default='default.jpg')
	img4 = models.ImageField("image 4",upload_to='post_images', default='default.jpg')
	#auto generated field
	date_posted = models.DateTimeField(default=timezone.now)

	def get_class(self):
	 	return self.__class__.__name__

	def __str__(self):
		return self.title

"""Stationery"""
class Stationery(Post):

	def get_absolute_url(self):
		return reverse('subcat-detail', kwargs={'pk': self.pk, 'model':'Stationery'})

	def __str__(self):
		return 'Stationery'

"""Electronics"""
class Electronics(Post):

	def get_absolute_url(self):
		return reverse('subcat-detail', kwargs={'pk': self.pk, 'model':'Electronics'})

	def __str__(self):
		return 'Electronics'

"""Furniture"""
class Furniture(Post):
	pass 

	def get_absolute_url(self):
		return reverse('subcat-detail', kwargs={'pk': self.pk, 'model':'Furniture'})

	def __str__(self):
		return 'Furniture'

"""Vehicle"""
class Vehicle(Post):
	pass 

	def get_absolute_url(self):
		return reverse('subcat-detail', kwargs={'pk': self.pk, 'model':'Vehicle'})

	def __str__(self):
		return 'Vehicle'

"""HouseHold"""
class HouseHold(Post): 

	def get_absolute_url(self):
		return reverse('subcat-detail', kwargs={'pk': self.pk, 'model':'HouseHold'})

	def __str__(self):
		return 'HouseHold'

"""Other"""
class Other(Post): 

	def get_absolute_url(self):
		return reverse('subcat-detail', kwargs={'pk': self.pk, 'model':'Other'})

	def __str__(self):
		return 'Other'

############################   NOT USED   #########################
"""Books"""
class BookCat(Post):
	pass 

	def get_absolute_url(self):
		return reverse('subcat-detail', kwargs={'pk': self.pk, 'model':'BookCat'})

	def __str__(self):
		return 'BookCat'

class Novel(BookCat):
	genre_list = 'Fiction Comedy Classic Biography Action Nonfiction Mystery Fantasy Drama'
	genre_CHOICES = func_CHOICES(genre_list)
	genre = models.CharField(max_length=lenn, choices=genre_CHOICES, default="Classic")
	novel_author = models.CharField(max_length=lenn, default="anonymous")

	def get_absolute_url(self):
		return reverse('subcat-detail', kwargs={'pk': self.pk, 'model':'Novel'})

	def __str__(self):
		return 'Novel'

class Engg(BookCat):
	branch_list = 'Computer Mechanical ENTC Chemical Civil ETX'
	branch_CHOICES = func_CHOICES(branch_list)
	branch = models.CharField(max_length=lenn, choices=branch_CHOICES, default="Computer")
	subject = models.CharField(max_length=lenn, default="Computer Networks")

	def get_absolute_url(self):
		return reverse('subcat-detail', kwargs={'pk': self.pk, 'model':'Engg'})

	def __str__(self):
		return 'Engg'

class School(BookCat):
	board_list = 'CBSE StateBoard other'
	board_CHOICES = func_CHOICES(board_list)
	board = models.CharField(max_length=lenn, choices=board_CHOICES, default="CBSE")
	std_list = '1 2 3 4 5 6 7 8 9 10 11 12'
	std_CHOICES = func_CHOICES(std_list)
	std = models.CharField(max_length=lenn, choices=std_CHOICES, default="12")
	subject = models.CharField(max_length=lenn, default="Math")

	def get_absolute_url(self):
		return reverse('subcat-detail', kwargs={'pk': self.pk, 'model':'School'})

	def __str__(self):
		return 'School'


"""Two Wheeler | Vehicles"""
class TwoWheeler(Post):#Vehicles
	#Bikes unique fields
	# sub_cat_CHOICES = [('Bikes', 'Bikes'), ('Scooty', 'Scooty'), ('Scooter', 'Scooter'),
	# ('Bicycle', 'Bicycle'), ('Other', 'Other')]
	km = models.PositiveIntegerField("KM", blank=True, null=True,  help_text='KM driven')
	cc = models.PositiveIntegerField("CC", blank=True, null=True,  help_text='CC')

	def get_absolute_url(self):
		return reverse('subcat-detail', kwargs={'pk': self.pk, 'model':'TwoWheeler'})

	def __str__(self):
		return 'TwoWheeler'
	
class Bike(TwoWheeler):
	brands_list = 'Bajaj Hero Honda Hero-honda KTM Yamaha Suzuki TVS Royal-Enfield Other'
	brand_CHOICES = func_CHOICES(brands_list)
	brand = models.CharField(max_length=lenn, choices=brand_CHOICES, default='Other')
	with_helmet = models.BooleanField(default=False)

	def get_absolute_url(self):
		return reverse('subcat-detail', kwargs={'pk': self.pk, 'model':'Bike'})

class Scooty(TwoWheeler):
	brands_list = 'Bajaj Hero Honda Mahindra Suzuki TVS Other'
	brand_CHOICES = func_CHOICES(brands_list)
	brand = models.CharField(max_length=lenn, choices=brand_CHOICES, default='Other')
	color = models.CharField(max_length=lenn, blank=True, null=True)

	def get_absolute_url(self):
		return reverse('subcat-detail', kwargs={'pk': self.pk, 'model':'Scooty'})

# class Bicycle(Post):
	# brands_list = 'Hercules Hero Other'
	# brand_CHOICES = func_CHOICES(brands_list)
	# brand = models.CharField(max_length=lenn, choices=brand_CHOICES, default='Other')
	# gears = models.PositiveIntegerField(blank=True, default=6, help_text="How many Gears?")

	# def get_absolute_url(self):
	# 	return reverse('subcat-detail', kwargs={'pk': self.pk, 'model':'Bicycle'})

"""Mobile/Charger/Cover"""
class MobileCat(Post):
	brands_list = 'Samsung Redmi Oppo Vivo iPhone MicroMax Other'
	brand_CHOICES = func_CHOICES(brands_list)
	brand = models.CharField(max_length=lenn, choices=brand_CHOICES, default='Other')

class Mobile(MobileCat):
	ram = models.PositiveIntegerField(blank=True, default=6, help_text="GB")
	internal_memory = models.PositiveIntegerField(blank=True, default=32, help_text="GB")
	front_camera = models.PositiveIntegerField(blank=True, default=32, help_text="MP")
	rear_camera = models.PositiveIntegerField(blank=True, default=32, help_text="MP")
	# how_old = models.PositiveIntegerField(blank=True, default=1, help_text="Months")

	def get_absolute_url(self):
		return reverse('subcat-detail', kwargs={'pk': self.pk, 'model':'Mobile'})

	def __str__(self):
		return 'Mobile'

class MobileCover(MobileCat):
	pass

class MobileCharger(MobileCat):
	port_type_CHOICES = [('type-C', 'type-C'), ('type-A', 'type-A'), ('other', 'other')]
	port_type = models.CharField(max_length=lenn, choices=port_type_CHOICES, default='other')
	original = models.BooleanField(default=False)
	cable_length = models.PositiveIntegerField(blank=True, null=True, help_text="metre")
	voltage = models.PositiveIntegerField(blank=True, null=True, help_text="Volts")
	ampere = models.PositiveIntegerField(blank=True, null=True, help_text="Ampere")

	def get_absolute_url(self):
		return reverse('subcat-detail', kwargs={'pk': self.pk, 'model':'MobileCharger'})

	def __str__(self):
		return 'MobileCharger'

"""Laptop"""
class LaptopCat(Post):
	pass

class Laptop(LaptopCat):
	brands_list = 'Lenovo Dell HP Vaio Mac Other'
	brand_CHOICES = func_CHOICES(brands_list)
	brand = models.CharField(max_length=lenn, choices=brand_CHOICES, default='Other')	 
	ram = models.PositiveIntegerField(blank=True, default=6, help_text="GB")
	internal_memory = models.PositiveIntegerField(blank=True, default=32, help_text="GB")
	processor = models.PositiveIntegerField(blank=True, default=5, help_text="core i5")
	cards_list = 'Intel Nvidia Radeon Zotac Other'
	cards_CHOICES = func_CHOICES(brands_list)
	internal_graphic_card = models.CharField(max_length=lenn, choices=cards_CHOICES, default='Other')
	iGB = models.PositiveIntegerField(blank=True, default=4, help_text="GB")
	external_graphic_card = models.CharField(max_length=lenn, choices=cards_CHOICES, default='Other')
	eGB = models.PositiveIntegerField(blank=True, default=4, help_text="GB")

	def get_absolute_url(self):
		return reverse('subcat-detail', kwargs={'pk': self.pk, 'model':'Laptop'})

	def __str__(self):
		return 'Laptop'

class Mouse(LaptopCat):
	brands_list = 'Lenovo Dell HP Viao Mac Other'
	brand_CHOICES = func_CHOICES(brands_list)
	brand = models.CharField(max_length=lenn, choices=brand_CHOICES, default='Other')	
	gaming = models.BooleanField(default=False)

	def get_absolute_url(self):
		return reverse('subcat-detail', kwargs={'pk': self.pk, 'model':'Mouse'})

	def __str__(self):
		return 'Mouse'

class Keyboard(LaptopCat):
	brands_list = 'Lenovo Dell HP Viao Mac Other'
	brand_CHOICES = func_CHOICES(brands_list)
	brand = models.CharField(max_length=lenn, choices=brand_CHOICES, default='Other')	
	gaming = models.BooleanField(default=False)

	def get_absolute_url(self):
		return reverse('subcat-detail', kwargs={'pk': self.pk, 'model':'Keyboard'})

	def __str__(self):
		return 'Keyboard'


# class Mobile(Post):
	#mobile unique fields
	# sub_cat_CHOICES = [('Mobile', 'Mobile'), ('Charger', 'Charger'), ('Cover', 'Cover'),
	# ('Earphone', 'Earphone/Headphone'), ('Other', 'Other')]
	# brand_CHOICES = [('Redmi', 'Redmi'), ('Vivo', 'Vivo'), ('OnePLus', 'OnePLus'), 
	# ('iPhone', 'iPhone'), ('Other', 'Other')]
	# brand = models.CharField(max_length=lenn, choices=brand_CHOICES, default='Redmi')




#****************************** ARCHIVE - OLD MODALS ****************************************#
# from django import template
# register = template.Library()

# class Common(models.Model):
# 	author = models.ForeignKey(User, on_delete=models.CASCADE)
# 	desc = models.TextField(blank=True)
# 	date_posted = models.DateTimeField(default=timezone.now)
# 	starred = models.BooleanField(default=False)

# 	class Meta:
# 		abstract = True


# class College(Common):
# 	Year_CHOICES=[('FY','I'),('SY','II'),('TY','III'),('BE','IV')]
# 	academic_year=models.CharField(max_length=lenn,choices=Year_CHOICES,default='I')
# 	Branch_CHOICES=[('CS','CS'),('Mech','Mech'),('ENTC','ENTC'),('IT','IT'),
# 	('CHEM','CHEM'),('ETX','ETX'),('Civil','Civil'),('FY','FY')]
# 	branch=models.CharField(max_length=lenn,choices=Branch_CHOICES,default='CS')
# 	Subject_CHOICES=[('NO SUBJECT','NO SUBJECT'),('DSF','Data Structures And Files'),('DSGT','Data Structures and Graph Theory'),('AM2','Applied Mathematcs'),
# 		('AM1','Applied Mechanics'),('EI','Engineering Informatics'),('DBMS','DBMS'),('SYSTEM ENGG','SYSTEM ENGG'),
# 		('MATHS','MATHS'),('PSYCHO','PSYCHO'),('MATERIAL ENGG','MATERIAL ENGG'),('PYTHON','PYTHON'),('CPP','CPP'),
# 		('EEE','EEE'),	('None','none')]	
# 	sub=models.CharField(max_length=lenn,choices=Subject_CHOICES,default='NO SUBJECT',
# 		help_text="if sub not in the list, write sub in sub_new")
# 	sub_new = models.CharField(max_length=100, blank=True,
# 		help_text="write full name of subject like not DEM but Digital Electronics and Microprocessors")
# 	# widget = {
# 	# 	'sub' : 

# 	# }
# 	#dependent forms
# 	# course_code = based on the subject, branch, year ,not taken from user

# 	class Meta:
# 		abstract = True

# class Enotes(College):
# 	#unique
# 	topic = models.CharField(max_length=100)
# 	unit = models.PositiveIntegerField(blank=True, default=1)
# 	Notes_author_CHOICES=[('teacher','Teacher'),('student','Student'),('other','Other')]
# 	notes_author = models.CharField(max_length=lenn,choices=Notes_author_CHOICES,default='Anonymous')
# 	author_name = models.CharField(max_length=100)
# 	#soft copy
# 	fileMy = models.FileField(upload_to='blog_pdf',blank=True)

# 	def __str__(self):
# 		return self.topic

# 	def get_absolute_url(self):
# 		return reverse('enotes-detail', kwargs={'pk': self.pk})
    
	
# class QuesPaper(College):
# 	#unique
# 	Sem_exam_CHOICES=[('ISE1','ISE1'),('ISE2','ISE2'),('MSE','MSE'),('ESE','ESE'),
# 	('ISE','ISE')]
# 	sem_exam = models.CharField(max_length=100,choices=Sem_exam_CHOICES,default='ESE')
# 	total_marks = models.PositiveIntegerField(blank=True, default=100)
# 	exam_date = models.DateTimeField(default=timezone.now, 
# 		help_text="YYYY-DD-MM")
# 	Exam_type_CHOICES = [ ('Regular', 'Regular'), ('Re-exam', 'Re-exam')]
# 	exam_type = models.CharField(max_length=100,choices=Exam_type_CHOICES,default='Rgular')
# 	#soft copy
# 	fileMy = models.FileField(upload_to='Ques_papers',blank=True)

# 	def __str__(self):
# 		return self.sem_exam

# 	def get_absolute_url(self):
# 		return reverse('ques-paper-detail', kwargs={'pk': self.pk})

# class Pracs(College):
# 	#unique
# 	topic = models.CharField(max_length=100)
# 	question = models.CharField(max_length=100)
# 	Pracs_author_CHOICES=[('teacher','Teacher'),('student','Student'),('other','Other')]
# 	pracs_author = models.CharField(max_length=lenn,choices=Pracs_author_CHOICES,default='Anonymous')
# 	author_name = models.CharField(max_length=100)
# 	#soft copy
# 	fileMy = models.FileField(upload_to='Pracs',blank=True)

# 	def __str__(self):
# 		return self.topic

# 	def get_absolute_url(self):
# 		return reverse('pracs-detail', kwargs={'pk': self.pk})


		