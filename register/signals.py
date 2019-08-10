#Notes on Signals, some like to add it directly to the models.py model, however django docs recommend this way.

from django.db.models.signals import post_save
#This is a signal that gets fired after and object gets saved.
from django.contrib.auth.models import User
#we want to fire this signal when a user gets created, we need the User model for this the user will be called the sender.
#as it is sending the signal.
from django.dispatch import receiver
#If there is a sender we need to create a reciever as a function that gets the signal and preforms a task
from .models import Profile
#we need the profile since we will be creating a profile in our function.

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
