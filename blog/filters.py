import django_filters

from . models import Enotes, QuesPaper, Pracs

class EnotesFilter(django_filters.FilterSet):

	topic = django_filters.CharFilter(lookup_expr='icontains',label='topic' )
	# author = django_filters.CharFilter(lookup_expr='icontains',label='posted by', field_name='author')
	author_name = django_filters.CharFilter(lookup_expr='icontains',label='created by')
	desc = django_filters.CharFilter(lookup_expr='icontains',label='Desc')
 
	class Meta:
		model = Enotes
		fields = (
			#4
			'topic',
			'unit',
			'notes_author',
		 	'author_name',
		 	#2
			'academic_year',
			'sub',
			'branch',
			#1
			'desc',
			'author'	
		)

class QuesPaperFilter(django_filters.FilterSet):

	total_marks = django_filters.CharFilter(lookup_expr='icontains',label='marks' )
	# author = django_filters.CharFilter(lookup_expr='icontains',label='posted by', field_name='author')
	# author_name = django_filters.CharFilter(lookup_expr='icontains',label='created by')
	desc = django_filters.CharFilter(lookup_expr='icontains',label='Desc')
 
	class Meta:
		model = QuesPaper
		fields = (
			#4
			'sem_exam',
			'total_marks',
			'exam_date',
		 	'exam_type',
		 	#2
			'academic_year',
			'sub',
			'branch',
			#1
			'desc',
			'author'	
		)

class PracsFilter(django_filters.FilterSet):

	topic = django_filters.CharFilter(lookup_expr='icontains',label='topic' )
	question = django_filters.CharFilter(lookup_expr='icontains',label='question', field_name='author')
	author_name = django_filters.CharFilter(lookup_expr='icontains',label='created by')
	desc = django_filters.CharFilter(lookup_expr='icontains',label='Desc')
 
	class Meta:
		model = Pracs
		fields = (
			#4
			'topic',
			'question',
			'pracs_author',
		 	'author_name',
		 	#2
			'academic_year',
			'sub',
			'branch',
			#1
			'desc',
			'author'	
		)











