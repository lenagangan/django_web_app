from __future__ import unicode_literals
from django.db import models
import os
from django.template.defaultfilters import slugify
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length = 120, db_index = True)
    slug = models.SlugField(max_length=150, unique = True, db_index=True, default = '', blank = True)
    posted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def save(self, *args, ** kwargs):
        if not self.pk:
            self.slug = slugify(self.name) #name become the slug
        super(Category, self).save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('products:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete = models.CASCADE)
    name = models.CharField(max_length = 120, db_index = True)
    slug = models.SlugField(max_length=100, db_index=True, default = '', blank = True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    available = models.BooleanField(default = True)

    def picture_path(self, title):
        return os.path.join ('static/store', str(title))
    picture = models.ImageField(upload_to = picture_path, blank= True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def save(self, *args, ** kwargs):
        if not self.pk:
            self.slug = slugify(self.name) #name become the slug
        super(Product, self).save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('products:product_detail', args=[self.id, self.slug])