from django.db import models

# Create your models here.
class User(models.Model):
	user_name=models.CharField(max_length=20)
	password=models.CharField(max_length=200)

	def __str__(self):
		return self.user_name
	def check_password(self,p):
		return p==self.password
