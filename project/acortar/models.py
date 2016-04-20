from __future__ import unicode_literals


from django.db import models


# class URLs acortadas
# utilizaremos id como identificador para acortar la URL

class Url(models.Model):
    original = models.CharField(max_length=32)
