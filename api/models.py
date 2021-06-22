from django.db import models

TYPE_CHOICES = [('texture', 'Texture'), ('audio', 'Audio')]


# Create your models here.
class Table(models.Model):
    type = models.CharField(choices=TYPE_CHOICES, max_length=10)
    tags = models.CharField(max_length=500)
    file = models.FileField(upload_to='',)
    disabled = models.BooleanField(verbose_name='Disabled')

    def __str__(self):
        return f'Type: {self.type}; Tags: {self.tags}; File: {self.file}; Disabled: {self.disabled}'
