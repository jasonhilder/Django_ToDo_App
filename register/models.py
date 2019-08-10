from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here. #Need to install library "Pillow" to work with images in python/django

#default django model doesnt have a field for a profile pic.
class Profile(models.Model): #need to add that field by extending the user model with a OneToOne model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics') #uploads to a directory.

    def __str__(self):
        return f'{self.user.username} Profile'

    #overide the save method
    def save(self, *args, **kwargs):
        #run the save method of the parent class.
        super().save(*args, **kwargs)

        #grab the image that was save and resize it.
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)