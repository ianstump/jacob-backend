from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# from project.api.categories.choices import categories_choices
# from .helpers import code_generator


class UserProfile(models.Model):
    location = models.CharField(
        verbose_name='location',
        max_length=25,
        null=True,
    )
    phone = models.IntegerField(
        verbose_name='phone',
        null=True,
    )

    profile_picture = models.URLField(
        verbose_name='profile_picture',
        null=True,
    )
    joined_date = models.DateTimeField(
        verbose_name='joined_date',
        auto_now_add=True,
    )
    validation_code = models.CharField(
        verbose_name='validation_code',
        help_text='random code used for registration and for password reset',
        max_length=15,
        default=code_generator

    )
    user = models.OneToOneField(
        verbose_name='user',
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user_profile',
    )

    def generate_new_code(self):
        self.validation_code = code_generator()
        self.save()

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.user_profile.save()