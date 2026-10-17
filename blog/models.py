from django.db import models
from django.utils.text import slugify

# Category model
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
      return self.name
    



# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img_url = models.URLField(null=True, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class AboutUs(models.Model):
    content = models.TextField()

    class Meta:
        verbose_name ="About Us"
        verbose_name_plural = "About Us"
