#urls.py

from django.conf.urls  import url

from . import  views

urlpatterns = [
    url(r'^$',views.archive,name = 'archive'),
    url(r'^create/$',views.create_blogpost,name='create_blogpost')
]