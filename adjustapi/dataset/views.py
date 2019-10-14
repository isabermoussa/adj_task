from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Sum
from django_filters import FilterSet
from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.exceptions import APIException
from url_filter.integrations.drf import DjangoFilterBackend

from adjustapi.serializers import UserSerializer, DatasetSerializer
from dataset.models import Dataset

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# ViewSets define the view behavior.
class DatasetViewSet(viewsets.ModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ['date', 'channel', 'country', 'os']
    ordering_fields = ['date', 'channel', 'country', 'os', 'impressions',
                       'clicks', 'installs', 'spend', 'revenue']

    def get_queryset(self):
        group_params = self.request.query_params.get('group_by')
        queryset = Dataset.objects.all()

        if group_params:
            group_fields = [x.strip() for x in group_params.split(',')]

            if len(list(set(group_fields) - set(self.filter_fields))) > 0 and len(group_fields) > 0:
                raise APIException('Wrong Params to group with!')

            queryset = queryset.values(*group_fields).annotate(impressions=Sum(
                'impressions'), clicks=Sum('clicks'),  installs=Sum('installs'), 
                spend=Sum('spend'), revenue=Sum('revenue'))
        return queryset
