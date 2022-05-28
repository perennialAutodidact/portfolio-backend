from django.db import models

class StoredFile(models.Model):
    file = models.FileField('file', upload_to='')

    def __str__(self):
        return self.file.name