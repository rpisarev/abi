from django.db import models
from django.contrib import admin
import PIL
import uuid, os, string
from PIL import Image
from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToFit, Adjust,ResizeToFill
from transmeta import TransMeta


class EventRecord(models.Model):
    __metaclass__ = TransMeta
    title = models.CharField(max_length = 160)
    title_side = models.CharField(max_length = 160)
    main_image = models.ForeignKey('EventImage', related_name = '+',  blank = True, null = True)
    descript = models.CharField(max_length = 120, blank = True)
    body = models.TextField()
    report = models.BooleanField()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['id']
        translate = ('title', 'title_side', 'descript', 'body')

class EventImage(models.Model):
    __metaclass__ = TransMeta

    def get_file_path(self, filename):
        extension = filename.split('.')[-1]
        filename = '%s.%s' % (uuid.uuid4(), extension)
        return os.path.join('images', filename)

    record = models.ForeignKey(EventRecord, related_name = 'images', blank = True)
    image = models.ImageField(upload_to = get_file_path, max_length = 256)
    name = models.CharField(max_length = 60)
    '''image(s) to PhotoReport'''

    def __unicode__(self):
        return self.name

    class Meta:
        translate = ('name', )



class SocNet(models.Model):

    ico = models.CharField(max_length = 10)
    url = models.URLField()

class EventRecordAdmin(admin.ModelAdmin):
    search_fields = ['title']

class EventImageAdmin(admin.ModelAdmin):
    search_fields = ['name']

class SocNetAdmin(admin.ModelAdmin):
    search_fields = ['url']


admin.site.register(EventRecord, EventRecordAdmin)
admin.site.register(EventImage, EventImageAdmin)
admin.site.register(SocNet, SocNetAdmin)
