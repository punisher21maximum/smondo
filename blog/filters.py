import django_filters

from .models import (Post, 
    Bike, Scooty, #Bicycle, 
    Mobile,  MobileCharger, #MobileCover,
    Laptop, Mouse, Keyboard,
    Novel, Engg, School
    )



class BikesFilter(django_filters.FilterSet):
	# common: price - 5, min max, year - min max, desc - contains
	title = django_filters.CharFilter(lookup_expr='icontains', label='Title')
	desc = django_filters.CharFilter(lookup_expr='icontains', label='Desc')
	year = django_filters.NumberFilter()
	year_min = django_filters.NumberFilter(field_name='year', lookup_expr='gte', label='Start year')
	year_max = django_filters.NumberFilter(field_name='year', lookup_expr='lte', label='End year')

	#
	sell_price = django_filters.NumberFilter()
	sell_price__gt = django_filters.NumberFilter(field_name='sell_price', lookup_expr='gte', label='sell price min')
	sell_price__lt = django_filters.NumberFilter(field_name='sell_price', lookup_expr='lte', label='sell price max')
	
	rent_hour = django_filters.NumberFilter()
	rent_hour__gt = django_filters.NumberFilter(field_name='rent_hour', lookup_expr='gte', label='rent hour min')
	rent_hour__lt = django_filters.NumberFilter(field_name='rent_hour', lookup_expr='lte', label='rent hour max')
	
	rent_day = django_filters.NumberFilter()
	rent_day__gt = django_filters.NumberFilter(field_name='rent_day', lookup_expr='gte', label='rent day min')
	rent_day__lt = django_filters.NumberFilter(field_name='rent_day', lookup_expr='lte', label='rent day max')
	
	rent_week = django_filters.NumberFilter()
	rent_week__gt = django_filters.NumberFilter(field_name='rent_week', lookup_expr='gte', label='rent week min')
	rent_week__lt = django_filters.NumberFilter(field_name='rent_week', lookup_expr='lte', label='rent week max')
	
	rent_month = django_filters.NumberFilter()
	rent_month__gt = django_filters.NumberFilter(field_name='rent_month', lookup_expr='gte', label='rent month min')
	rent_month__lt = django_filters.NumberFilter(field_name='rent_month', lookup_expr='lte', label='rent month max')
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

class ScootysFilter(django_filters.FilterSet):
	# common: price - 5, min max, year - min max, desc - contains
	title = django_filters.CharFilter(lookup_expr='icontains', label='Title')
	desc = django_filters.CharFilter(lookup_expr='icontains', label='Desc')
	year = django_filters.NumberFilter()
	year_min = django_filters.NumberFilter(field_name='year', lookup_expr='gte', label='Start year')
	year_max = django_filters.NumberFilter(field_name='year', lookup_expr='lte', label='End year')

	#
	sell_price = django_filters.NumberFilter()
	sell_price__gt = django_filters.NumberFilter(field_name='sell_price', lookup_expr='gte', label='sell price min')
	sell_price__lt = django_filters.NumberFilter(field_name='sell_price', lookup_expr='lte', label='sell price max')
	
	rent_hour = django_filters.NumberFilter()
	rent_hour__gt = django_filters.NumberFilter(field_name='rent_hour', lookup_expr='gte', label='rent hour min')
	rent_hour__lt = django_filters.NumberFilter(field_name='rent_hour', lookup_expr='lte', label='rent hour max')
	
	rent_day = django_filters.NumberFilter()
	rent_day__gt = django_filters.NumberFilter(field_name='rent_day', lookup_expr='gte', label='rent day min')
	rent_day__lt = django_filters.NumberFilter(field_name='rent_day', lookup_expr='lte', label='rent day max')
	
	rent_week = django_filters.NumberFilter()
	rent_week__gt = django_filters.NumberFilter(field_name='rent_week', lookup_expr='gte', label='rent week min')
	rent_week__lt = django_filters.NumberFilter(field_name='rent_week', lookup_expr='lte', label='rent week max')
	
	rent_month = django_filters.NumberFilter()
	rent_month__gt = django_filters.NumberFilter(field_name='rent_month', lookup_expr='gte', label='rent month min')
	rent_month__lt = django_filters.NumberFilter(field_name='rent_month', lookup_expr='lte', label='rent month max')
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

class MobilesFilter(django_filters.FilterSet):
	# common: price - 5, min max, year - min max, desc - contains
	title = django_filters.CharFilter(lookup_expr='icontains', label='Title')
	desc = django_filters.CharFilter(lookup_expr='icontains', label='Desc')
	year = django_filters.NumberFilter()
	year_min = django_filters.NumberFilter(field_name='year', lookup_expr='gte', label='Start year')
	year_max = django_filters.NumberFilter(field_name='year', lookup_expr='lte', label='End year')

	#
	sell_price = django_filters.NumberFilter()
	sell_price__gt = django_filters.NumberFilter(field_name='sell_price', lookup_expr='gte', label='sell price min')
	sell_price__lt = django_filters.NumberFilter(field_name='sell_price', lookup_expr='lte', label='sell price max')
	
	rent_hour = django_filters.NumberFilter()
	rent_hour__gt = django_filters.NumberFilter(field_name='rent_hour', lookup_expr='gte', label='rent hour min')
	rent_hour__lt = django_filters.NumberFilter(field_name='rent_hour', lookup_expr='lte', label='rent hour max')
	
	rent_day = django_filters.NumberFilter()
	rent_day__gt = django_filters.NumberFilter(field_name='rent_day', lookup_expr='gte', label='rent day min')
	rent_day__lt = django_filters.NumberFilter(field_name='rent_day', lookup_expr='lte', label='rent day max')
	
	rent_week = django_filters.NumberFilter()
	rent_week__gt = django_filters.NumberFilter(field_name='rent_week', lookup_expr='gte', label='rent week min')
	rent_week__lt = django_filters.NumberFilter(field_name='rent_week', lookup_expr='lte', label='rent week max')
	
	rent_month = django_filters.NumberFilter()
	rent_month__gt = django_filters.NumberFilter(field_name='rent_month', lookup_expr='gte', label='rent month min')
	rent_month__lt = django_filters.NumberFilter(field_name='rent_month', lookup_expr='lte', label='rent month max')
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











