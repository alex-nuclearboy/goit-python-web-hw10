from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    """
    Profile model extends the built-in User model with additional data.

    Attributes:
        user (OneToOneField): A one-to-one link to Django's User model.
                              Ensures each user instance has one, and only one,
                              associated Profile instance.
        avatar (ImageField): A field to upload profile images,
                             with a default image specified.

    Methods:
        __str__(self):
            Returns the username of the user associated with this profile.
        save(self, *args, **kwargs):
            Extends the default save method by adding functionality to resize
            the uploaded image to a maximum of 250x250 pixels if necessary.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        default='default_avatar.png',
        upload_to='profile_images'
    )

    def __str__(self):
        """
        Return the username of the user associated with this profile.
        """
        return self.user.username

    def save(self, *args, **kwargs):
        """
        Save the instance and resize the uploaded image to a maximum
        of 250x250 pixels, if the image dimensions exceed this size.
        """
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 250 or img.width > 250:
            new_img = (250, 250)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
