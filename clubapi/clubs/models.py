# Base club model
from django.db import models


class Club(models.Model):
    name = models.CharField(max_length=64)
    nickname = models.CharField(max_length=64)
    description = models.TextField()
    found_date = models.IntegerField(default=1920)
    stadium = models.CharField(max_length=64)
    stadium_capacity = models.IntegerField(default=45000)
    number_of_titles = models.IntegerField()
    crest = models.ImageField(upload_to='crests', default=None)

    # function added to recognize clubs easier in admin site
    def __str__(self):
        return self.name
