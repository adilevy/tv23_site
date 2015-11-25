from django.db import models

class Series(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    from_year = models.SmallIntegerField()
    to_year = models.SmallIntegerField()
    '''todo : add link to image   '''

class Season(models.Model):
    name = models.CharField(max_length=200)
    series = models.ForeignKey(Series)
    year = models.SmallIntegerField()
    '''todo : add link to image   '''

class Asset(models.Model):
    system_id = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    series = models.ForeignKey(Season)
    episode = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    synopsys = models.CharField(max_length=200)
    audience = models.CharField(max_length=200)
    genres = models.CharField(max_length=200)
    primo_url = models.CharField(max_length=200)
    thumbnail_url = models.CharField(max_length=200)
    entry_id = models.CharField(max_length=200)
    video_url = models.CharField(max_length=200)
    clean_records = models.CharField(max_length=200)


