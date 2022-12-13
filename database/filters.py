import django_filters

from database.models import Student


class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = ['group']


# {
#             : ['AIN-1-22', 'AIN-2-22', 'MIN-1-22', 'WIN-1-22'],
#         }

