from django.db import models


class Event(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    date = models.DateField()
    place = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name[0:50]

    class Meta:
        db_table = 'event'
