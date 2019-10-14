from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from django.db.models import Sum
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
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['date', 'channel', 'country', 'os']

    def get_queryset(self):
        queryset = Dataset.objects.all()
        group_by = self.request.query_params.get('group_by', '')
        sort_by = self.request.query_params.get('sort_by', '')
        if len(group_by) > 0:
            pass
        
        if len(sort_by) > 0:
            pass
         
        
        return Dataset.objects.group_by('channel', 'country').distinct()