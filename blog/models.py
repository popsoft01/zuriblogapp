from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title


# class CommentModel(models.Model):
#     author = models.CharField(max_length=20)
#     comment_text = models.TextField()
#     comment_time = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reversed('post_detail', args=[str(self.id)])
