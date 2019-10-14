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
    cpi = serializers.SerializerMethodField('calculate_cpi')
    date = serializers.DateField(required=False)
    channel = serializers.CharField(required=False, allow_blank=True)
    country = serializers.CharField(required=False, allow_blank=True)
    os = serializers.CharField(required=False, allow_blank=True)


    def calculate_cpi(self, obj):
        if type(obj) == type(dict()):
            return obj.get('spend') / obj.get('installs')
        else:
            return obj.spend / obj.installs
    class Meta:
        model = Dataset
        fields = ('id', 'date', 'channel', 'country', 'os', 'impressions', 
                  'clicks', 'installs', 'spend', 'revenue', 'cpi')
