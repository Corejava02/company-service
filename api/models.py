from django.db import models

# Create your models here.

class Company(models.Model):
    end_year=models.CharField(max_length=200)
    intensity=models.CharField(max_length=200)
    sector=models.CharField(max_length=200)
    topic=models.CharField(max_length=200)
    insight=models.CharField(max_length=200)
    url=models.CharField(max_length=200)
    start_year=models.CharField(max_length=200)
    impact=models.CharField(max_length=200)
    added=models.CharField(max_length=200)
    published=models.CharField(max_length=200)
    pestle=models.CharField(max_length=200)
    source=models.CharField(max_length=200)
    title=models.CharField(max_length=200)
    likelihood=models.CharField(max_length=200)
    relevance=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    region=models.CharField(max_length=200)

