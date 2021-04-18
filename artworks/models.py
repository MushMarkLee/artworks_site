from django.db import models




class Artworks(models.Model):
    title = models.CharField('Title', max_length=50)
    anons = models.CharField('Intro', max_length=250)
    description = models.TextField('Desc', max_length=250)
    img = models.ImageField(upload_to='artworks/static/artworks/media/', null=True,blank=True)


    def __str__(self):
        return "%s" % self.id

