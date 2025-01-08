from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
import re
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='mountains.jpg', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            base_slug = re.sub(r'[^a-z0-9-]', '', base_slug)
            base_slug = base_slug[:50]
            slug = base_slug
            counter = 1

            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title