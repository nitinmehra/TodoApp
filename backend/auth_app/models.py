from django.db import models
from django.contrib.auth.models import AbstractUser

# User roles
class User(AbstractUser):
	ADMIN = 1
	USER = 2

	ROLE_CHOICES = (
		(ADMIN, 'Admin'),
		(USER, 'User'),
	)

	role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
	# You can create Role model separately and add ManyToMany if user has more than one role