from django.db import models

class Source(models.Model):
	judgeId = models.IntegerField()
	userId = models.CharField(max_length=100)
	problemId = models.CharField(max_length=100)
	language = models.CharField(max_length=100)
	version = models.CharField(max_length=100)
	submissionDate = models.BigIntegerField()
	judgeDate = models.BigIntegerField()
	cpuTime = models.IntegerField()
	memory = models.IntegerField()
	codeSize = models.IntegerField()
	server = models.IntegerField()
	policy = models.CharField(max_length=100)
	rating = models.IntegerField()
	review = models.IntegerField()
	sourceCode = models.TextField()
	submissionDateString=""
	cpuTimeString=""
	problemName=""
class Paiza_API(models.Model):
	sourceCode=models.TextField()
	language=models.CharField(max_length=100)