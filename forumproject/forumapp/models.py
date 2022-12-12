from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.urls import reverse

STATUS = (
    (1, 'Draft'),
    (2, 'Published'),
)
# Create your models here.


class Forum(models.Model):
    title = models.CharField(max_length=55)
    header = models.CharField(max_length=55, blank=True, null=True)
    slug = models.SlugField(max_length=55,unique=True)
    body = models.TextField()
    status = models.IntegerField(choices=STATUS, default=1)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(default=now)

    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('forum:post_details', kwargs={'get_slug':self.slug})


class Comment(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name='comments')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body