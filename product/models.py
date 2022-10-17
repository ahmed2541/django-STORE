from ast import Pass
from datetime import datetime
from distutils.command import upload
from email.mime import image
from email.policy import default
from pickle import TRUE
from random import choice
from re import T
from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse

# Create your models here.






class Category(models.Model):
    name = models.CharField(max_length=50,default='')


    def __str__(self):
        return self.name

##ITEM
class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(null=True,blank=True)
    category = models.ManyToManyField(Category)
    description = models.TextField()
    image = models.ImageField(upload_to='image_itrems/%y/%m/%d')
    slug = models.SlugField(null=True,blank=True)
    
    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug =slugify(self.title) 
        super(Item,self).save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('product:product_detail',kwargs={'slug':self.slug})

#### ORDER ITEM #####
class OrderItem(models.Model):
    Pass

    

    




    def __str__(self):
        return self.title


class OrderItem(models.Model):
    pass

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    pass

    def __str__(self):
        return self.name