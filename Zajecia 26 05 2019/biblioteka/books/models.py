from django.db import models

# Create your models here.
COVER_TYPES = (
    ('soft', 'miekka'),
    ('hard', 'twarda'),
)

class Book(models.Model):
    title = models.CharField(max_length=150)
    description=models.TextField(null=True,blank=True)
    cover_type = models.CharField(max_length=20,choices=COVER_TYPES,default='hard')
    author = models.ForeignKey('authors.Author', on_delete=models.DO_NOTHING,null=True,blank=True,related_name='books')

    def __str__(self):
        return  f"{self.id} | {self.title}"
