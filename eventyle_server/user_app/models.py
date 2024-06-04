from django.db import models
from djongo import models as djongo_models


# class ProfileInfo(UserProfileInfo):
#     user_id = models.UUIDField(primary_key=True, editable=False)
#     name = models.TextField()
#     surname = models.TextField()
#     role = models.TextField()
#     description = models.TextField()
#
#     class Meta:
#         db_table = 'user'

class ProfilePost(models.Model):
    post_id = models.UUIDField(primary_key=True)
    user_id = models.UUIDField()
    post_text = models.TextField()

    class Meta:
        db_table = 'post'


class PostImage(models.Model):
    post_id = models.UUIDField(primary_key=True)
    image_id = models.UUIDField()

    class Meta:
        db_table = 'post_image'


class ProfilePostImage(models.Model):
    _id = models.TextField(primary_key=True)
    image = models.BinaryField()

    class Meta:
        db_table = 'post_img'
