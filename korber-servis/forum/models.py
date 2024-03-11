from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("name"))
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', verbose_name=_("parent category"))
    
    def __str__(self):
        return self.name   
    
    class Meta:
        verbose_name_plural = 'categories'
        
class Document(models.Model):
	pdfFile = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='documents')
	name = models.CharField(max_length=50, verbose_name=_("documents"), null=True)
	file = models.FileField(upload_to='documents/')
	created_at = models.DateTimeField(auto_now_add=True)
     
	def __str__(self):
		return self.file.name
     

class Post(models.Model):
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    content = models.TextField(blank=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    closed_comments = models.BooleanField(default=False)

    def __str__(self):
        return str(self.content[:20])


    def num_comments(self):
        return self.comment_set.all().count()

    class Meta:
        ordering = ('-created',)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(max_length=300, blank=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)
    
def media_upload_to(instance, filename):
    return f"media/{instance.post.category}/{filename}"


class Media(models.Model):
    post = models.ForeignKey(Post, related_name='media', on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey(Comment, related_name='media', on_delete=models.CASCADE, null=True, blank=True)
    file = models.FileField(upload_to=media_upload_to, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'mp4', 'mov', 'avi'])])

    def save(self, *args, **kwargs):
        if self.post and self.comment:
            raise ValueError("Media cannot be associated with both a post and a comment.")
        super().save(*args, **kwargs)
