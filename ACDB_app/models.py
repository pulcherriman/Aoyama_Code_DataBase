from django.db import models

class Source(models.Model):
	judgeId = models.IntegerField()
	userId = models.CharField()
	problemId = models.CharField()
	language = models.CharField()
	version = models.CharField()
	submissionDate = models.BigIntegerField()
	judgeDate = models.BigIntegerField()
	cpuTime = models.IntegerField()
	memory = models.IntegerField()
	codeSize = models.IntegerField()
	server = models.IntegerField()
	policy = models.CharField()
	rating = models.IntegerField()
	review = models.IntegerField()
	code = models.TextField()
