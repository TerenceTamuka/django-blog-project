from django.db import models
#from datetime import datetime




# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    

    def __str__(self):
        return self.title
