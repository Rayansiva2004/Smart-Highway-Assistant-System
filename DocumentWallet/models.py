from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=255, verbose_name="Document Title")
    document = models.FileField(upload_to='documents/', verbose_name="Uploaded Document")  # Using FileField to store files
    user_id = models.CharField(max_length=255, null=True, blank=True, verbose_name="User ID")  # Changed to CharField

    class Meta:
        db_table = 'document_wallet'  # Set the custom table name

    def __str__(self):
        return self.title
