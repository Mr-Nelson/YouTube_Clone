from django.db import models


class Comment(models.Model):
    author = models.CharField(max_length=50)
    text = models.TextField(max_length=300)
    likes = models.IntegerField()
    video_key = models.CharField(max_length=50)
    # subComment = models.ForeignKey(models.Model.Comment.pk)

    def __str__(self):
        return f"{self.author}, {self.text}"
