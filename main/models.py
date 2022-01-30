from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse

class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        orginal_slug = slugify(self.title)
        queryset = Tag.objects.all().filter(slug__iexact=orginal_slug).count()

        count = 1
        slug = orginal_slug
        while(queryset):
            slug = orginal_slug + '-' + str(count)
            count += 1
            queryset = Tag.objects.all().filter(slug__iexact=slug).count()
        
        self.slug = slug

        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Article(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE,  null=True, blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField()
    title = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        orginal_slug = slugify(self.title)
        queryset = Article.objects.all().filter(slug__iexact=orginal_slug).count()

        count = 1
        slug = orginal_slug
        while(queryset):
            slug = orginal_slug + '-' + str(count)
            count += 1
            queryset = Article.objects.all().filter(slug__iexact=slug).count()
        
        self.slug = slug

        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(':detail', args=[self.slug, ])
