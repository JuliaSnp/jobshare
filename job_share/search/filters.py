from django.contrib.auth.models import User

from accounts.models import UserProfile

import django_filters

#based on the code from https://simpleisbetterthancomplex.com/tutorial/2016/11/28/how-to-filter-querysets-dynamically.html

class ProfileFilter(django_filters.FilterSet):
    skills = django_filters.CharFilter(lookup_expr='icontains')
    pers_summary = django_filters.CharFilter(lookup_expr='icontains')
    target_partner = django_filters.CharFilter(lookup_expr='icontains')
    industry = django_filters.CharFilter(lookup_expr='icontains')
    position = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = UserProfile
        fields = (
                'pers_summary',
                'target_partner',
                'skills',
                'industry',
                'employed',
                'position',
                'years_exp'
            )
