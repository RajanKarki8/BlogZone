from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length= 255,blank=True, null=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    desc = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.post}, {self.author}'
    
