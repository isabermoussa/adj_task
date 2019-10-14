from django.db import models
from django.db.models.query import QuerySet
from django_group_by import GroupByMixin


class DatasetQuerySet(QuerySet, GroupByMixin):
    pass


class Dataset(models.Model):
    objects = DatasetQuerySet.as_manager()
    
    date = models.DateField()
    channel = models.CharField(max_length=255)
    country = models.CharField(max_length=50)
    os = models.CharField(max_length=100)
    impressions = models.IntegerField()
    clicks = models.IntegerField()
    installs = models.IntegerField()
    spend = models.DecimalField(max_digits=9, decimal_places=3)
    revenue = models.DecimalField(max_digits=9, decimal_places=3)
    
    def __str__(self):
        return "{} - {}".format(self.channel, self.country)

    def save(self, *args, **kwargs):
        super(Dataset, self).save(*args, **kwargs)

    class Meta:
        ordering = ["-date"]
