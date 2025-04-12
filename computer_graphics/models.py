'''Django models for internal database'''
from django.db import models


class FunctionGL(models.Model):
    '''Django model for OpenGL function'''
    username = models.TextField()
    email = models.EmailField()
    signature = models.TextField()
    description = models.TextField()
    feature = models.TextField()


class FunctionVK(models.Model):
    '''Django model for Vulkan function'''
    username = models.TextField()
    email = models.EmailField()
    signature = models.TextField()
    description = models.TextField()
    feature = models.TextField()


class Feedback(models.Model):
    '''Django model for user feedback message'''
    username = models.TextField()
    email = models.EmailField()
    feedback = models.TextField()
