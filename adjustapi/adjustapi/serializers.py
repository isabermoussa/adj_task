from rest_framework import serializers

from django.contrib.auth.models import User
from dataset.models import Dataset


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


# Serializers define the API representation.
class DatasetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dataset
        fields = ('id', 'date', 'channel', 'country', 'os', 'impressions', 
                  'clicks', 'installs', 'spend', 'revenue')
