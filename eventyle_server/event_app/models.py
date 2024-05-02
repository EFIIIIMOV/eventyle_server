from django.db import models


class Event(models.Model):
    event_id = models.UUIDField(primary_key=True, editable=False)
    name = models.TextField()
    date = models.DateField()
    place = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name[0:50]

    class Meta:
        db_table = 'event'


class EventInfo(models.Model):
    info_id = models.UUIDField(primary_key=True, editable=False)
    event_id = models.UUIDField(editable=False)
    name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name[0:50]

    class Meta:
        db_table = 'event_info'


class EventImage(models.Model):
    _id = models.TextField(primary_key=True)
    image = models.BinaryField()

    class Meta:
        db_table = 'event_image'


class UserEvent(models.Model):
    user_id = models.UUIDField()
    event_id = models.UUIDField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user_id', 'event_id'], name='user_event_unique_constraint')
        ]
        db_table = 'user_event'
