# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import  permalink

# Create your models here.
class BlogPost (models.Model) :
    title = models.CharField(max_length=150,unique= True)
    author = models.CharField(max_length=100,default="",unique= True)
    slug = models.SlugField(max_length=100,unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True,auto_now_add=True)
    #timestamp = models.DateTimeField()

    def _unicode_(self):
        return '%s' % self.title

    #返回博客链接
    @permalink
    def get_absolute_url(self):
        return ('view_blog_post',None,{'slug':self.slug})