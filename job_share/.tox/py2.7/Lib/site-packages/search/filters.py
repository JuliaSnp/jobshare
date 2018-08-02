from django.contrib.auth.models import User

from accounts.models import UserProfile

import django_filters

#class UserFilter(django_filters.FilterSet):
    #class Meta:
        #model = User
        #fields = ['username', 'first_name', 'last_name', ]


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
