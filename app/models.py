from django.db import models

class File(models.Model):
    upload = models.FileField(default=None)
    uploaded_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.upload.name


    
