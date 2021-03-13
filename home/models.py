from django.db import models

# Create your models here.
class User(models.Model):
	user_name=models.CharField(max_length=20,primary_key=True)
	password=models.CharField(max_length=200)

	def __str__(self):
		return self.user_name
	def check_password(self,p):
		return p==self.password

class Social_accounts(models.Model):
	user_name=models.ForeignKey(User,on_delete=models.CASCADE)
	website_name = models.CharField(max_length=50)
	profile_url = models.URLField(max_length=200)

	def __str__(self):
		return self.website_name