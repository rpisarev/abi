from django.db import models
from django.contrib import admin
import PIL
import uuid, os, string
from PIL import Image
from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToFit, Adjust,ResizeToFill
from transmeta import TransMeta


class PortfCateg(models.Model):
    __metaclass__ = TransMeta
    name = models.CharField(max_length = 30)
    name_in_uri = models.CharField(max_length = 30)

    def __unicode__(self):
        return self.name

    class Meta:
        translate = ('name', )

class PortfRecord(models.Model):
    __metaclass__ = TransMeta
    title = models.CharField(max_length = 60)
    url = models.CharField(max_length = 60)
    created = models.DateTimeField(auto_now_add = True)
    main_image = models.ForeignKey('PortfImage', related_name = '+',  blank = True, null = True)
    category = models.ForeignKey(PortfCateg, related_name = 'records')

    def __unicode__(self):
        return self.title

    def get_url(self):
        return str(self.url)

    class Meta:
        ordering = ['created']
        translate = ('title', )

class PortfImage(models.Model):

    def get_file_path(self, filename):
        extension = filename.split('.')[-1]
        filename = '%s.%s' % (uuid.uuid4(), extension)
        return os.path.join('images', filename)

    record = models.ForeignKey(PortfRecord, related_name = 'images', blank = True)
    image = models.ImageField(upload_to = get_file_path, max_length = 256)
    name = models.CharField(max_length = 60)
    image_small = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1),
        ResizeToFill(120, 120)], image_field = 'image',
        format = 'JPEG', options = {'quality': 90})
    image_medium = ImageSpecField([Adjust(contrast = 1.2, sharpness = 1.1),
        ResizeToFit(260, 260)], image_field = 'image',
        format = 'JPEG', options = {'quality': 90})
    image_big = ImageSpecField([Adjust(contrast = 1.2, sharpness = 1.1),
        ResizeToFit(640, 480)], image_field = 'image',
        format = 'JPEG', options = {'quality': 90})
    '''image(s) to portfolio'''

    def __unicode__(self):
        return self.name



class PortfRecordAdmin(admin.ModelAdmin):
    search_fields = ['title']

class PortfImageAdmin(admin.ModelAdmin):
    search_fields = ['name']


class PortfCategAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(PortfRecord, PortfRecordAdmin)
admin.site.register(PortfImage, PortfImageAdmin)
admin.site.register(PortfCateg, PortfCategAdmin)
