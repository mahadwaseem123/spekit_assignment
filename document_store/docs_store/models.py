from django.db import models

# Create your models here.


class Topic(models.Model):
    short_desc = models.CharField(max_length=255)
    long_desc = models.TextField()

    def __str__(self):
        return self.short_desc


class BaseDocument(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    topics = models.ManyToManyField(Topic, related_name='%(class)s_topics')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Folder(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Document(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    topics = models.ManyToManyField(Topic)

    def __str__(self):
        return self.name

