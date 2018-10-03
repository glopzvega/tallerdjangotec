from django.db import models

# Create your models here.

class Book(models.Model):
	# languages = [
	# 	("spanish", "Español"),
	# 	("english", "Inglés")]

	title = models.CharField(max_length=255)
	author = models.CharField(max_length=255)
	content_short = models.TextField(null=True, blank=True)
	publisher = models.CharField(max_length=255, null=True)
	publisher_date = models.CharField(max_length=4, null=True)
	pages = models.IntegerField(default=0)
	language = models.CharField(max_length=45, null=True)
	image = models.ImageField(null=True, blank=True)

	def __str__(self):
		# return self.title + "," + self.author
		return "%s , %s" % (self.title, self.author)
