
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

# class User(models.Model):
# 	username = models.CharField(max_length=20, unique=True),
# 	password = models.CharField(max_length=20),
# 	email = models.CharField(max_length=50, unique=True),
	# address = models.CharField(max_length=100, unique=True),
	# created_at = models.DateTimeField(editable=False)
	# updated_at = models.DateTimeField()


class UserProfile(models.Model):
	# UserProfile is linked to a User model (built-in, being imported from dj library)
	user = models.OneToOneField(User)
	# User can add his/ her bio (about me section)
	# user_bio = models.CharField(max_length=250, default=None)

	def __str__(self):
		return self.user.username


	def save(self, *args, **kwargs):
		self.updated_at = timezone.now()
		if not self.id:
			self.created_at = timezone.now()
		super().save(*args, **kwargs)
