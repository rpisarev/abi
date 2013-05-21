from django.db import models
from django.contrib import admin
from transmeta import TransMeta


class MainMenuItem(models.Model):
    __metaclass__ = TransMeta
    text = models.CharField(max_length = 12)
    url = models.CharField(max_length = 30)
    back_image = models.CharField(max_length = 10, blank = True, null = True)

    def __unicode__(self):
        return self.text

    class Meta:
        translate = ('text', )

class MainMenuPage(models.Model):
    __metaclass__ = TransMeta
    body = models.TextField()
    title = models.CharField(max_length = 60)
    item =  models.ForeignKey(MainMenuItem)
    class Meta:
        translate = ('body', 'title',)

class MainMenuItemAdmin(admin.ModelAdmin):
    search_fields = ['name']

class MainMenuPageAdmin(admin.ModelAdmin):
    search_fields = ['title']

admin.site.register(MainMenuItem, MainMenuItemAdmin)
admin.site.register(MainMenuPage, MainMenuPageAdmin)


