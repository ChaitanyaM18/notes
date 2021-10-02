from django.db import models

class QRModel(models.Model):
    image_path = models.CharField(max_length=20)
    image_name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.image_path} Image'
