from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, **kwargs):
        super().save()

        pic = Image.open(self.profile_pic.path)

        if pic.height > 300 or pic.width > 300:
            output_size = (300, 300)
            pic.thumbnail(output_size)
            pic.save(self.profile_pic.path)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
