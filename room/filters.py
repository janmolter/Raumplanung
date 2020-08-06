import django_filters
from .models import Raum


class RaumFilter(django_filters.FilterSet):

	class Meta:
		model = Raum
		fields = ['Anzahl_Sitzplaetze','Whiteboard', 'Beamer']