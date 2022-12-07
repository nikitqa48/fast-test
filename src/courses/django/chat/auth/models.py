from django.db import models


class Model(models.Model):
    xz = models.CharField(max_length=500, blank=True, null=True)