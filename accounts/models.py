from __future__ import unicode_literals

from django.db import models
#image upload file directory creation
def user_directory_path(instance, filename):
	return 'user_{0}/{1}/'.format(instance.userName	, filename)

# Create your models here.
class UserAccounts(models.Model):
	email = models.CharField(max_length=100)
	password = models.CharField(max_length=15)
	first_name = models.CharField(max_length=255, null=True, blank=True)
	last_name = models.CharField(max_length=255, null=True, blank=True)
	image = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
	created = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)

	class Meta:
		db_table = 'usr_accounts'


