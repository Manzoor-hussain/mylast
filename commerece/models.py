import datetime

from django.contrib.auth.models import Permission, User

# Create your models here.
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
from django.utils import cache

from mylast import settings
from django.db import models
#from django.geoposition.fields import GeopositionField
#from django.geopy.geocoders import GoogleV3

class PointOfInterest(models.Model):
    name = models.CharField(max_length=100)
 #   position = GeopositionField()

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.album_title + "--- " + self.artist


# def _str_(self):
#   return self.album_title ,+ '-' + self.artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=250)
    song_title = models.CharField(max_length=250)
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title + "--- " + self.file_type
#class product (models.Model):
class Test(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=500)
    def __str__(self):
        return self.first_name + "--- " + self.last_name

    def __str__(self):
        return self.first_name + "--- " + self.last_name
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=40, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    mobile_number = models.CharField(max_length=10,null=True)
    image = models.ImageField(upload_to='profile_picture')

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.user.username

    def last_seen(self):
        return cache.get('last_seen_%s' % self.user.username)

    def online(self):
        if self.last_seen():
            now = datetime.datetime.now()
            if now > (self.last_seen() + datetime.timedelta(seconds=settings.USER_ONLINE_TIMEOUT)):
                return False
            else:
                return True
        else:
            return False
class Contact(models.Model):
    name=models.CharField(max_length=100,blank=True)
    mobile_number=models.CharField(max_length=11,blank=True)
    messsage=models.TextField(max_length=300, blank=True)
    sender_mail=models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    register_user_key=models.IntegerField(null=True,blank=True)
class Conversation(models.Model):
    post_key=models.IntegerField()
    user_one=models.IntegerField()
    user_two=models.IntegerField()

class Chat(models.Model):
    conversation=models.ForeignKey(Conversation, related_name='convers',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    message= models.TextField(max_length=500, blank=True)
    sender=models.IntegerField()


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    post_key = models.IntegerField()
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    group_id=models.IntegerField()
    sender_name=models.CharField(max_length=200 ,null=True)
    receiver_name=models.CharField(max_length=200,null=True)
    sender_image=models.CharField(max_length=400, null=True)
    receiver_image=models.CharField(max_length=400,null=True)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ('-timestamp',)


