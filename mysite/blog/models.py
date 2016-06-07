# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    # title=title.decode('utf-8')
    text = models.TextField()
    # test=text.decode('utf-8')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
        #jiang'def  __str__(self)'改成'def  __unicode__(self)'以处理保存中文字符后出现的UnicodeEncodeError: 'ascii' codec can't encode characters 
    def  __unicode__(self):
        return self.title