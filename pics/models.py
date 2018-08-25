from django.db import models
import os
import datetime
from django.utils import timezone
from django.template.defaultfilters import slugify


class Post(models.Model):
    title = models.CharField(max_length = 100, blank = True) 
    text_body = models.TextField(blank=True)
    slug = models.SlugField(max_length=255,unique=True, blank = True) 
    def picture_path(self, title):
        return os.path.join ('static/img', str(title))
    picture = models.ImageField(upload_to = picture_path, blank= True)
    pub_date = models.DateTimeField('date posted', blank=True)

    def was_published_recently(self):
       return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.title

    def save(self, *args, ** kwargs):
        if not self.pk:
            self.slug = slugify(self.title) #title become the slug
        super(Post, self).save(*args,**kwargs)
