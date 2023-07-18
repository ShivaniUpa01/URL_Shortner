from django.db import models


# Create your models here.
class url_shortner(models.Model):
    original_url = models.URLField
