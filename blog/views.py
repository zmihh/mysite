# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from datetime import  datetime
from  django.shortcuts import render,render_to_response
from blog.models import BlogPost
from django.http import  HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.template import  RequestContext


def archive (request):
    #post = BlogPost(title='morktitile',body='mockbody', timestamp = datetime.now())
    post = BlogPost.objects.all().order_by('-timestamp')
    context = {'data':post }
    return render(request,'blog/archive.html',context)


def create_blogpost(request):
    if request.method == 'POST':
        BlogPost (
            title = request.POST.get('title'),
            body = request.POST.get('body'),
            timestamp = datetime.now(),

        ).save()
    #return HttpResponseRedirect('/blog/')
    return render_to_response('blog/archive.html',{'post':BlogPost},RequestContext(request))