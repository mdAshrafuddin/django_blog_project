from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = (
    (0, 'Darft'),
    (1, 'Published')
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author  = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs_post')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.title