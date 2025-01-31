from django.db import models

class TODO(models.Model):
    title = models.CharField(max_length=100) 
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title