from django.db import models


class Chat(models.Model):
    chat_id = models.UUIDField(primary_key=True, editable=False)
    name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name[0:50]

    class Meta:
        db_table = 'chat'


class ChatImage(models.Model):
    _id = models.TextField(primary_key=True)
    image = models.BinaryField()

    class Meta:
        db_table = 'chat_image'


class UserChat(models.Model):
    user_id = models.UUIDField(primary_key=True)
    chat_id = models.UUIDField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user_id', 'chat_id'], name='user_chat_unique_constraint')
        ]
        db_table = 'user_chat'


class Message(models.Model):
    message_id = models.UUIDField(primary_key=True)
    chat_id = models.UUIDField()
    user_id = models.UUIDField()
    message_text = models.TextField()
    create_time = models.DateTimeField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['message_id', 'chat_id', 'user_id'],
                                    name='message_chat_user_unique_constraint')
        ]
        db_table = 'message'
