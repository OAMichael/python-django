from django.db import models


class FunctionGL(models.Model):
    username = models.TextField()
    email = models.EmailField()
    signature = models.TextField()
    description = models.TextField()
    feature = models.TextField()


class FunctionVK(models.Model):
    username = models.TextField()
    email = models.EmailField()
    signature = models.TextField()
    description = models.TextField()
    feature = models.TextField()


class Feedback(models.Model):
    username = models.TextField()
    email = models.EmailField()
    feedback = models.TextField()