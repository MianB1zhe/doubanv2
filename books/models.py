from __future__ import unicode_literals

from django.db import models

# Create your models here.

# the user info at douban
class DoubanUser(models.Model):
    user_id = models.CharField(max_length = 20, primary_key = True)
    user_uid = models.CharField(max_length = 20)
    name = models.CharField(max_length = 40)
    created_at_douban = models.DateTimeField()
    loc_name = models.CharField(max_length = 20)
    # photo url = 'https://img3.doubanio.com/' + avatar
    # large photo = url.replace('icon/u','icon/up')
    avatar = models.CharField(max_length = 40)  
    signature = models.CharField(max_length = 200, null = True)
    desc = models.CharField(max_length = 200, null = True)
    created_at = models.DateTimeField()
    access_times = models.IntegerField()

    def __unicode__(self):
        return self.name

# the book info at douban
class DoubanBook(models.Model):
    book_id = models.CharField(max_length = 20, primary_key = True)
    title = models.CharField(max_length = 40)
    subtitle = models.CharField(max_length = 40, null = True)
    author = models.CharField(max_length = 40)
    isbn13 = models.CharField(max_length = 20)
    price = models.CharField(max_length = 20, null = True)
    pages = models.IntegerField()
    rating = models.FloatField()
    num_raters = models.IntegerField()
    pubdate = models.DateTimeField()
    publisher = models.CharField(max_length = 40)
    tags = models.TextField()
    # image url = '"https://img3.doubanio.com/mpic/' + image
    # for small large medium image, use spic,lpic,mpic
    image = models.CharField(max_length = 20)

    def __unicode__(self):
        return self.title

# user read books info
class UserReadBooks(models.Model):
    id = models.AutoField(primary_key = True)
    user_id = models.ForeignKey(DoubanUser, on_delete = models.CASCADE)
    book_id = models.ForeignKey(DoubanBook, on_delete = models.DO_NOTHING)
    updated = models.DateTimeField()
    rating = models.FloatField()
    comment = models.TextField(null = True)
    tags = models.CharField(max_length = 100, null = True)

    def __unicode__(self):
        return self.user_id.name + ' : ' + self.book_id.title