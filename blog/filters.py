import django_filters

from .models import (Post, 
    Bike, Scooty, #Bicycle, 
    Mobile,  MobileCharger, #MobileCover,
    Laptop, Mouse, Keyboard,
    Novel, Engg, School
    )

from django.forms.widgets import TextInput

class CommonFilter(django_filters.FilterSet):
	# common: price - 5, min max, year - min max, desc - contains
	title = django_filters.CharFilter(lookup_expr='icontains', label='Title', 
	widget=TextInput(attrs={'placeholder': 'search bikes...'}))
	desc = django_filters.CharFilter(lookup_expr='icontains', label='Desc', 
	widget=TextInput(attrs={'placeholder': 'search description...'}))
	year = django_filters.NumberFilter()
	year_min = django_filters.NumberFilter(field_name='year', lookup_expr='gte', label='Start year', 
	widget=TextInput(attrs={'placeholder': 'start'}))
	year_max = django_filters.NumberFilter(field_name='year', lookup_expr='lte', label='End year', 
	widget=TextInput(attrs={'placeholder': 'end'}))

	#
	sell_price = django_filters.NumberFilter()
	sell_price__gt = django_filters.NumberFilter(field_name='sell_price', lookup_expr='gte', label='sell price min', 
	widget=TextInput(attrs={'placeholder': 'min'}))
	sell_price__lt = django_filters.NumberFilter(field_name='sell_price', lookup_expr='lte', label='sell price max', 
	widget=TextInput(attrs={'placeholder': 'max'}))
	
	rent_hour = django_filters.NumberFilter()
	rent_hour__gt = django_filters.NumberFilter(field_name='rent_hour', lookup_expr='gte', label='rent hour min', 
	widget=TextInput(attrs={'placeholder': 'min'}))
	rent_hour__lt = django_filters.NumberFilter(field_name='rent_hour', lookup_expr='lte', label='rent hour max', 
	widget=TextInput(attrs={'placeholder': 'max'}))
	
	rent_day = django_filters.NumberFilter()
	rent_day__gt = django_filters.NumberFilter(field_name='rent_day', lookup_expr='gte', label='rent day min', 
	widget=TextInput(attrs={'placeholder': 'min'}))
	rent_day__lt = django_filters.NumberFilter(field_name='rent_day', lookup_expr='lte', label='rent day max', 
	widget=TextInput(attrs={'placeholder': 'max'}))
	
	rent_week = django_filters.NumberFilter()
	rent_week__gt = django_filters.NumberFilter(field_name='rent_week', lookup_expr='gte', label='rent week min', 
	widget=TextInput(attrs={'placeholder': 'min'}))
	rent_week__lt = django_filters.NumberFilter(field_name='rent_week', lookup_expr='lte', label='rent week max', 
	widget=TextInput(attrs={'placeholder': 'max'}))
	
	rent_month = django_filters.NumberFilter()
	rent_month__gt = django_filters.NumberFilter(field_name='rent_month', lookup_expr='gte', label='rent month min', 
	widget=TextInput(attrs={'placeholder': 'min'}))
	rent_month__lt = django_filters.NumberFilter(field_name='rent_month', lookup_expr='lte', label='rent month max', 
	widget=TextInput(attrs={'placeholder': 'max'}))


class BikesFilter(CommonFilter):
	# # common: price - 5, min max, year - min max, desc - contains
	# title = django_filters.CharFilter(lookup_expr='icontains', label='Title', 
	# widget=TextInput(attrs={'placeholder': 'search bikes...'}))
	# desc = django_filters.CharFilter(lookup_expr='icontains', label='Desc', 
	# widget=TextInput(attrs={'placeholder': 'search description...'}))
	# year = django_filters.NumberFilter()
	# year_min = django_filters.NumberFilter(field_name='year', lookup_expr='gte', label='Start year', 
	# widget=TextInput(attrs={'placeholder': 'start'}))
	# year_max = django_filters.NumberFilter(field_name='year', lookup_expr='lte', label='End year', 
	# widget=TextInput(attrs={'placeholder': 'end'}))

	# #
	# sell_price = django_filters.NumberFilter()
	# sell_price__gt = django_filters.NumberFilter(field_name='sell_price', lookup_expr='gte', label='sell price min', 
	# widget=TextInput(attrs={'placeholder': 'min'}))
	# sell_price__lt = django_filters.NumberFilter(field_name='sell_price', lookup_expr='lte', label='sell price max', 
	# widget=TextInput(attrs={'placeholder': 'max'}))
	
	# rent_hour = django_filters.NumberFilter()
	# rent_hour__gt = django_filters.NumberFilter(field_name='rent_hour', lookup_expr='gte', label='rent hour min', 
	# widget=TextInput(attrs={'placeholder': 'min'}))
	# rent_hour__lt = django_filters.NumberFilter(field_name='rent_hour', lookup_expr='lte', label='rent hour max', 
	# widget=TextInput(attrs={'placeholder': 'max'}))
	
	# rent_day = django_filters.NumberFilter()
	# rent_day__gt = django_filters.NumberFilter(field_name='rent_day', lookup_expr='gte', label='rent day min', 
	# widget=TextInput(attrs={'placeholder': 'min'}))
	# rent_day__lt = django_filters.NumberFilter(field_name='rent_day', lookup_expr='lte', label='rent day max', 
	# widget=TextInput(attrs={'placeholder': 'max'}))
	
	# rent_week = django_filters.NumberFilter()
	# rent_week__gt = django_filters.NumberFilter(field_name='rent_week', lookup_expr='gte', label='rent week min', 
	# widget=TextInput(attrs={'placeholder': 'min'}))
	# rent_week__lt = django_filters.NumberFilter(field_name='rent_week', lookup_expr='lte', label='rent week max', 
	# widget=TextInput(attrs={'placeholder': 'max'}))
	
	# rent_month = django_filters.NumberFilter()
	# rent_month__gt = django_filters.NumberFilter(field_name='rent_month', lookup_expr='gte', label='rent month min', 
	# widget=TextInput(attrs={'placeholder': 'min'}))
	# rent_month__lt = django_filters.NumberFilter(field_name='rent_month', lookup_expr='lte', label='rent month max', 
	# widget=TextInput(attrs={'placeholder': 'max'}))
	#
	km = django_filters.NumberFilter()
	km__gt = django_filters.NumberFilter(field_name='km', lookup_expr='gte', label='km min')
	km__lt = django_filters.NumberFilter(field_name='km', lookup_expr='lte', label='km max')

	cc = django_filters.NumberFilter()
	cc__gt = django_filters.NumberFilter(field_name='cc', lookup_expr='gte', label='cc min')
	cc__lt = django_filters.NumberFilter(field_name='cc', lookup_expr='lte', label='cc max')

	class Meta:
		model = Bike
		fields = (
			# common
			# 'author',
			'title',
			'desc',
		 	'year',
			# 'date_posted',
		 	# #
			'sell_price',
			'rent_hour',
			'rent_day',
			'rent_week',
			'rent_month',
			# # TwoWheeler
			# 'km', 
			# 'cc',
			# # Bike
			# 'brand', 
			# 'with_helmet'
		)

class ScootysFilter(CommonFilter):
	# # common: price - 5, min max, year - min max, desc - contains
	# title = django_filters.CharFilter(lookup_expr='icontains', label='Title')
	# desc = django_filters.CharFilter(lookup_expr='icontains', label='Desc')
	# year = django_filters.NumberFilter()
	# year_min = django_filters.NumberFilter(field_name='year', lookup_expr='gte', label='Start year')
	# year_max = django_filters.NumberFilter(field_name='year', lookup_expr='lte', label='End year')

	# #
	# sell_price = django_filters.NumberFilter()
	# sell_price__gt = django_filters.NumberFilter(field_name='sell_price', lookup_expr='gte', label='sell price min')
	# sell_price__lt = django_filters.NumberFilter(field_name='sell_price', lookup_expr='lte', label='sell price max')
	
	# rent_hour = django_filters.NumberFilter()
	# rent_hour__gt = django_filters.NumberFilter(field_name='rent_hour', lookup_expr='gte', label='rent hour min')
	# rent_hour__lt = django_filters.NumberFilter(field_name='rent_hour', lookup_expr='lte', label='rent hour max')
	
	# rent_day = django_filters.NumberFilter()
	# rent_day__gt = django_filters.NumberFilter(field_name='rent_day', lookup_expr='gte', label='rent day min')
	# rent_day__lt = django_filters.NumberFilter(field_name='rent_day', lookup_expr='lte', label='rent day max')
	
	# rent_week = django_filters.NumberFilter()
	# rent_week__gt = django_filters.NumberFilter(field_name='rent_week', lookup_expr='gte', label='rent week min')
	# rent_week__lt = django_filters.NumberFilter(field_name='rent_week', lookup_expr='lte', label='rent week max')
	
	# rent_month = django_filters.NumberFilter()
	# rent_month__gt = django_filters.NumberFilter(field_name='rent_month', lookup_expr='gte', label='rent month min')
	# rent_month__lt = django_filters.NumberFilter(field_name='rent_month', lookup_expr='lte', label='rent month max')
	# #

	title = django_filters.CharFilter(lookup_expr='icontains', label='Title', 
	widget=TextInput(attrs={'placeholder': 'search scooty...'}))

	km = django_filters.NumberFilter()
	km__gt = django_filters.NumberFilter(field_name='km', lookup_expr='gte', label='km min')
	km__lt = django_filters.NumberFilter(field_name='km', lookup_expr='lte', label='km max')

	cc = django_filters.NumberFilter()
	cc__gt = django_filters.NumberFilter(field_name='cc', lookup_expr='gte', label='cc min')
	cc__lt = django_filters.NumberFilter(field_name='cc', lookup_expr='lte', label='cc max')

	class Meta:
		model = Scooty
		fields = (
			# common
			# 'author',
			'title',
			'desc',
		 	'year',
			# 'date_posted',
		 	# #
			'sell_price',
			'rent_hour',
			'rent_day',
			'rent_week',
			'rent_month',
			# # TwoWheeler
			# 'km', 
			# 'cc',
			# # Bike
			# 'brand', 
			# 'with_helmet'
		)

class MobilesFilter(CommonFilter):

	title = django_filters.CharFilter(lookup_expr='icontains', label='Title', 
	widget=TextInput(attrs={'placeholder': 'search mobile...'}))

	class Meta:
		model = Mobile
		fields = (
			# common
			# 'author',
			'title',
			'desc',
		 	'year',
			# 'date_posted',
		 	# #
			'sell_price',
			'rent_hour',
			'rent_day',
			'rent_week',
			'rent_month',
			# # TwoWheeler
			# 'km', 
			# 'cc',
			# # Bike
			# 'brand', 
			# 'with_helmet'
		)

class MobileChargersFilter(CommonFilter):

	title = django_filters.CharFilter(lookup_expr='icontains', label='Title', 
	widget=TextInput(attrs={'placeholder': 'search chargers...'}))

	class Meta:
		model = MobileCharger
		fields = (
			# common
			# 'author',
			'title',
			'desc',
		 	'year',
			# 'date_posted',
		 	# #
			'sell_price',
			'rent_hour',
			'rent_day',
			'rent_week',
			'rent_month',
			# # TwoWheeler
			# 'km', 
			# 'cc',
			# # Bike
			# 'brand', 
			# 'with_helmet'
		)

class NovelsFilter(CommonFilter):
	title = django_filters.CharFilter(lookup_expr='icontains', label='Title', 
	widget=TextInput(attrs={'placeholder': 'search novels...'}))

	class Meta:
		model = Novel
		fields = (
			# common
			# 'author',
			'title',
			'desc',
		 	'year',
			# 'date_posted',
		 	# #
			'sell_price',
			'rent_hour',
			'rent_day',
			'rent_week',
			'rent_month',
			# # TwoWheeler
			# 'km', 
			# 'cc',
			# # Bike
			# 'brand', 
			# 'with_helmet'
		)
#
class LaptopsFilter(CommonFilter):
	title = django_filters.CharFilter(lookup_expr='icontains', label='Title', 
	widget=TextInput(attrs={'placeholder': 'search laptop...'}))
	class Meta:
		model = Laptop
		fields = (
			# common
			# 'author',
			'title',
			'desc',
		 	'year',
			# 'date_posted',
		 	# #
			'sell_price',
			'rent_hour',
			'rent_day',
			'rent_week',
			'rent_month',
			# # TwoWheeler
			# 'km', 
			# 'cc',
			# # Bike
			# 'brand', 
			# 'with_helmet'
		)

class MousesFilter(CommonFilter):
	title = django_filters.CharFilter(lookup_expr='icontains', label='Title', 
	widget=TextInput(attrs={'placeholder': 'search mouse...'}))
	class Meta:
		model = Mouse
		fields = (
			# common
			# 'author',
			'title',
			'desc',
		 	'year',
			# 'date_posted',
		 	# #
			'sell_price',
			'rent_hour',
			'rent_day',
			'rent_week',
			'rent_month',
			# # TwoWheeler
			# 'km', 
			# 'cc',
			# # Bike
			# 'brand', 
			# 'with_helmet'
		)

class KeyboardsFilter(CommonFilter):
	title = django_filters.CharFilter(lookup_expr='icontains', label='Title', 
	widget=TextInput(attrs={'placeholder': 'search keyboard...'}))
	class Meta:
		model = Keyboard
		fields = (
			# common
			# 'author',
			'title',
			'desc',
		 	'year',
			# 'date_posted',
		 	# #
			'sell_price',
			'rent_hour',
			'rent_day',
			'rent_week',
			'rent_month',
			# # TwoWheeler
			# 'km', 
			# 'cc',
			# # Bike
			# 'brand', 
			# 'with_helmet'
		)

class EnggsFilter(CommonFilter):
	title = django_filters.CharFilter(lookup_expr='icontains', label='Title', 
	widget=TextInput(attrs={'placeholder': 'search engg books...'}))
	class Meta:
		model = Engg
		fields = (
			# common
			# 'author',
			'title',
			'desc',
		 	'year',
			# 'date_posted',
		 	# #
			'sell_price',
			'rent_hour',
			'rent_day',
			'rent_week',
			'rent_month',
			# # TwoWheeler
			# 'km', 
			# 'cc',
			# # Bike
			# 'brand', 
			# 'with_helmet'
		)

class SchoolsFilter(CommonFilter):
	title = django_filters.CharFilter(lookup_expr='icontains', label='Title', 
	widget=TextInput(attrs={'placeholder': 'search school books...'}))

	class Meta:
		model = School
		fields = (
			# common
			# 'author',
			'title',
			'desc',
		 	'year',
			# 'date_posted',
		 	# #
			'sell_price',
			'rent_hour',
			'rent_day',
			'rent_week',
			'rent_month',
			# # TwoWheeler
			# 'km', 
			# 'cc',
			# # Bike
			# 'brand', 
			# 'with_helmet'
		)





# class EnotesFilter(django_filters.FilterSet):

# 	topic = django_filters.CharFilter(lookup_expr='icontains',label='topic' )
# 	# author = django_filters.CharFilter(lookup_expr='icontains',label='posted by', field_name='author')
# 	author_name = django_filters.CharFilter(lookup_expr='icontains',label='created by')
# 	desc = django_filters.CharFilter(lookup_expr='icontains',label='Desc')
 
# 	class Meta:
# 		model = Enotes
# 		fields = (
# 			#4
# 			'topic',
# 			'unit',
# 			'notes_author',
# 		 	'author_name',
# 		 	#2
# 			'academic_year',
# 			'sub',
# 			'branch',
# 			#1
# 			'desc',
# 			'author'	
# 		)

# class QuesPaperFilter(django_filters.FilterSet):

# 	total_marks = django_filters.CharFilter(lookup_expr='icontains',label='marks' )
# 	# author = django_filters.CharFilter(lookup_expr='icontains',label='posted by', field_name='author')
# 	# author_name = django_filters.CharFilter(lookup_expr='icontains',label='created by')
# 	desc = django_filters.CharFilter(lookup_expr='icontains',label='Desc')
 
# 	class Meta:
# 		model = QuesPaper
# 		fields = (
# 			#4
# 			'sem_exam',
# 			'total_marks',
# 			'exam_date',
# 		 	'exam_type',
# 		 	#2
# 			'academic_year',
# 			'sub',
# 			'branch',
# 			#1
# 			'desc',
# 			'author'	
# 		)

# class PracsFilter(django_filters.FilterSet):

# 	topic = django_filters.CharFilter(lookup_expr='icontains',label='topic' )
# 	question = django_filters.CharFilter(lookup_expr='icontains',label='question', field_name='author')
# 	author_name = django_filters.CharFilter(lookup_expr='icontains',label='created by')
# 	desc = django_filters.CharFilter(lookup_expr='icontains',label='Desc')
 
# 	class Meta:
# 		model = Pracs
# 		fields = (
# 			#4
# 			'topic',
# 			'question',
# 			'pracs_author',
# 		 	'author_name',
# 		 	#2
# 			'academic_year',
# 			'sub',
# 			'branch',
# 			#1
# 			'desc',
# 			'author'	
# 		)











