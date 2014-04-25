from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    gang = models.ForeignKey('Gang', related_name='gangsters')
    tags_created = models.IntegerField(default=0)
    tags_deleted = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    busted = models.IntegerField(default=0)
    busts = models.IntegerField(default=0)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    mood = models.CharField(max_length=100, blank=True, null=True)
    last_action =  models.DateTimeField(blank=True, null=True)
    spraying = models.IntegerField(default=0)
    bustedviapolice = models.IntegerField(default=0)

    def __unicode__(self):
        return self.user.username

    def _get_ranking(self):
        "Returns the user's ranking."
        #TODO: Fix this
        #return '%s %s' % (self.first_name, self.last_name) TODO: create function
        return '#1'

    def _get_full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.user.first_name, self.user.last_name)

    full_name = property(_get_full_name)
    ranking = property(_get_ranking)


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

class Gang(models.Model):

    COLOR_CHOICES = (
        ('purple', 'Purple'),
        ('green', 'Green'),
        ('blue', 'Blue'),
    )

    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100, choices=COLOR_CHOICES)


    def __unicode__(self):
        return self.name


class Venue(models.Model):
    CATEGORY_CHOICES = (
        ('Ou', 'Great Outdoors'),
        ('Ni', 'Nightlife Spots'),
        ('Ar', 'Arts & Entertainment'),
        ('Ed', 'Education'),
        ('Fo', 'Food'),
        ('Ot', 'Other Places'),
        ('Sh', 'Shops & Services'),
        ('Tr', 'Travel & Transport'),
    )
    name = models.CharField(max_length=100)
    gangster = models.ForeignKey(UserProfile, blank=True, null=True, related_name='venues')
    gangsterSpraying = models.IntegerField(default = 0)
    gang = models.CharField(max_length=20)
    latestEditTimestamp = models.DateTimeField(blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    sprayinginitialized = models.IntegerField(default=0)


    class Meta:
        ordering = ('-latestEditTimestamp',)
        get_latest_by = 'latestEditTimestamp'

    def __unicode__(self):
        return self.name

class Message(models.Model):
    gangster = models.ForeignKey(UserProfile, related_name='messages')
    timestamp = models.DateTimeField()
    text = models.TextField()

    class Meta:
        ordering = ('-timestamp',)

    def __unicode__(self):
        return self.text
