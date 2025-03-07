from django.db import models
from django.contrib.auth import models as auth_model
from django.utils import timezone
from django.urls import reverse


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250)
    text1 = models.TextField()
    text2 = models.TextField(blank=True,null=True)
    middle_text = models.TextField(blank = True,null=True)
    title_image1_main = models.ImageField()
    title_image2 = models.ImageField(blank = True,null=True)
    title_image3 = models.ImageField(blank = True,null=True)
    title_image3 = models.ImageField(blank = True,null=True)
    create_date = models.DateTimeField(default=timezone.now())
    publish_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approve_comments(self):
        return self.comments.filter(approved_comments=True)


class Comment(models.Model):
    post = models.ForeignKey('blog.Post',related_name='comment',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('blog:post-list')
