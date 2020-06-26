from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, Profile_Student, Profile_Teacher


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
		lenn_mitaoe = len('@mitaoe.ac.in')
		if instance.email.endswith('@mitaoe.ac.in') :
			Profile_Student.objects.create(user=instance)
		else:
			Profile_Teacher.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

