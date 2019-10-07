from django.db import models
from django.utils import timezone
class Post(models.Model):
    name_d = models.CharField(max_length=20)
    image_d = models.ImageField(upload_to= 'images/', null=True)
    text_d = models.TextField()
    pub_date = models.DateTimeField('Дата', default=timezone.now)
    last_pub_date = models.DateTimeField('Дата')
    class Meta:
            ordering = ['-last_pub_date',]



class Comment(models.Model):
    image_d = models.ImageField()
    image_d = models.ImageField(upload_to= 'images/', blank=True)
    text_d = models.TextField()
    pub_date = models.DateTimeField('Дата', default=timezone.now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name=u"Пост", related_name="comments")
    class Meta:
        ordering = ['pub_date',]


# Create your models here.
