from django.db import models


class BlogModel(models.Model):

    blog_title = models.CharField(max_length=30)
    blog_time = models.DateTimeField(auto_now_add=True)
    blog_description = models.TextField()


    def __str__(self):
        return self.blog_title
    


    

 