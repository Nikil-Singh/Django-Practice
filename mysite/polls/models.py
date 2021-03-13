import datetime

from django.db import models
from django.utils import timezone
from django.db.models import signals
from django.dispatch import receiver 
from django.db.models.signals import pre_save, post_save

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        was_published_recently.admin_order_field = 'pub_date'
        was_published_recently.boolean = True
        was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

# Pre-save signal.    
def check_vote_pre(sender, instance, **kwargs):
    print("Pre-save: Vote made")

# Post-save signal
def check_vote_post(sender, instance, **kwargs):
    print("Post-save: Vote made")

pre_save.connect(check_vote_pre, sender=Choice)
post_save.connect(check_vote_post, sender=Choice)