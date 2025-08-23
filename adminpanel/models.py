from django.db import models
from cloudinary.models import CloudinaryField

class Adoption(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = CloudinaryField('image', null=True, blank=True)  # Fixed field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
