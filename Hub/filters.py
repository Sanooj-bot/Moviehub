import django_filters
from django_filters import DateFilter, CharFilter
from Hub.models import User,Movies

# User Filter to search in User Table
class UserFilter(django_filters.FilterSet):
	email = CharFilter(field_name='email', lookup_expr='icontains')

	class Meta:
		model = User
		fields = ('username', 'email')
		exclude = ('username')

# Movie Filter for Search in Movie Table
class MovieFilter(django_filters.FilterSet):
	moviename = CharFilter(field_name = 'moviename', lookup_expr='icontains')
	
	class Meta:
		model = User
		fields = ('moviename', 'movie_heading')
		exclude = ('movie_heading')