from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class MyLink(models.Model):
    url = models.CharField(max_length=100)
    desc = models.CharField(max_length=1024, blank=True)
    source = models.CharField(max_length=1024, blank=True)
    owner = models.ForeignKey(Owner, null=True, blank=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag)
