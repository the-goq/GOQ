from django.db import models
from django.utils import timezone
from django.urls import reverse

class Contact(models.Model):
	name= models.CharField(max_length=75)
	email = models.EmailField()
	message = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)



	def __str__(self):
		return self.email

class Questions(models.Model):
	name = models.CharField(max_length=125)
	level = models.CharField(max_length=75)
	year = models.IntegerField()
	faculty = models.CharField(max_length=75)
	semester = models.IntegerField()
	subject = models.CharField(max_length=100)
	date_posted = models.DateTimeField(default=timezone.now)
	file = models.FileField()

	def get_absolute_url(self):
		return reverse('detail', kwargs={'pk':self.pk})

	def __str__(self):
		return self.name

class Subject(models.Model):
	sName = models.CharField(max_length=75)
	level = models.CharField(max_length=75)
	faculty = models.CharField(max_length=75)
	semester = models.IntegerField(null=True, blank =True)


	def __str__(self):
		return self.sName

class QuestionFiles(models.Model):
	sName = models.ForeignKey(Subject, on_delete= models.CASCADE)
	year = models.IntegerField()
	date_posted = models.DateTimeField(default=timezone.now)
	file = models.FileField()

	def __str__(self):
		return self.sName.sName