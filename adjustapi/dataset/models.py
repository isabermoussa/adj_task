from django.db import models

class Dataset(models.Model):
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

    class Meta:
        ordering = ["-date"]
