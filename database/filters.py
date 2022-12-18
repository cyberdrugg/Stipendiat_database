import django_filters

from .models import *


class StudentFilter22(django_filters.FilterSet):
    class Meta:
        model = Students_22
        fields = ["group"]


class StudentFilter21(django_filters.FilterSet):
    class Meta:
        model = Students_21
        fields = ["group"]


class StudentFilter20(django_filters.FilterSet):
    class Meta:
        model = Students_20
        fields = ["group"]


class StudentFilter19(django_filters.FilterSet):
    class Meta:
        model = Students_19
        fields = ["group"]
