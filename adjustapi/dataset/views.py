from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
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
