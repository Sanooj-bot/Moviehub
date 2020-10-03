import django_filters
from django_filters import DateFilter, CharFilter

from Hub.models import User,Movies

class UserFilter(django_filters.FilterSet):
	username = CharFilter(field_name = 'username', lookup_expr='icontains')
	email = CharFilter(field_name='email', lookup_expr='icontains')
	class Meta:
		model = User
		fields = ('username','email')
class MovieFilter(django_filters.FilterSet):
	moviename = CharFilter(field_name = 'moviename', lookup_expr='icontains')
	
	class Meta:
		model = User
		fields = ('moviename','movie_heading')
		exclude = ('movie_heading')