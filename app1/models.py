from django.db import models
from django.utils.text import slugify

# Create your models here.

class Kategori(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self) -> str:
        return f'{self.name}'

class Postimi(models.Model):
    kategoria = models.ForeignKey(Kategori,on_delete=models.DO_NOTHING)
    titulli = models.CharField(max_length=150, null=False)
    pershkrimi = models.TextField(max_length=500, null=False)
    imazhi = models.ImageField(upload_to='postimet',null=True)
    slug = models.SlugField()

    def save(self,*args,**kwargs):
        self.slag = slugify (f'{self.titulli}')
        super(Postimi,self).save(*args,**kwargs)

    def __str__(self) -> str:
        return f'{self.titulli}'