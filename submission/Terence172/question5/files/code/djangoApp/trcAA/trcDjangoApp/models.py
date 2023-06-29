from django.db import models

# Create your models here.

class Tweet(models.Model):
    _id = models.CharField(max_length=255, primary_key=True)
    text = models.TextField(db_index=True)
    in_reply_to_status_id = models.CharField(max_length=255, null=True)
    retweet_count = models.IntegerField(null=True)
    contributors = models.CharField(max_length=255, null=True)
    created_at = models.CharField(max_length=255)
    geo = models.CharField(max_length=255, null=True)
    source = models.CharField(max_length=255)
    coordinates = models.CharField(max_length=255, null=True)
    in_reply_to_screen_name = models.CharField(max_length=255, null=True)
    truncated = models.BooleanField()
    entities = models.JSONField()
    retweeted = models.BooleanField(db_index=True)
    place = models.CharField(max_length=255, null=True)
    user = models.JSONField()
    favorited = models.BooleanField()
    in_reply_to_user_id = models.CharField(max_length=255, null=True)
    id = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'db_tweet'