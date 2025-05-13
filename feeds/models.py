from django.db import models
from django.contrib.auth.models import User

class Feed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_feeds', blank=True)

    def __str__(self):
        return f"{self.user.username}: {self.content[:50]}..."
    
    def like_count(self):
        return self.likes.count()