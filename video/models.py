from django.core.urlresolvers import reverse
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name



class Series(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    from_year = models.SmallIntegerField(null=True)
    to_year = models.SmallIntegerField(null=True)
    genre = models.ManyToManyField(Genre,related_name="appears_in_series",blank=True)
    '''todo : add link to image   '''
    def __str__(self):
        return self.name
    def thumbnail(self):
        return self.asset_set.first().thumbnail_url



class Season(models.Model):
    series = models.ForeignKey(Series)
    year = models.SmallIntegerField(null=True)
    def __str__(self):
        return self.year
    '''todo : add link to image   '''



class Asset(models.Model):
    system_id = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    series = models.ForeignKey(Series,null=True)
    season = models.ForeignKey(Season,null=True)
    episode = models.IntegerField(default=1)
    title = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    synopsys = models.CharField(max_length=200)
    audience = models.CharField(max_length=200,null=True)
    genres = models.ManyToManyField(Genre,related_name="appears_in_assets",blank=True)
    primo_url = models.CharField(max_length=200)
    thumbnail_url = models.CharField(max_length=200)
    entry_id = models.CharField(max_length=50)
    video_url = models.CharField(max_length=300)
    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse("video",args=(self.id,))
