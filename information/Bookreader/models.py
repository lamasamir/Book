from django.db import models
from django.utils import timezone

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=40)
    genre = models.CharField(max_length=60)
    des = models.TextField()
    book_coverimage = models.ImageField(upload_to='book_coverimage/', blank=True,null=True)
    author = models.CharField(max_length=30)
    content_pdf = models.FileField(upload_to='book_pdfs/', blank=True, null=True) 
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return self.title 


class User_Data(models.Model):
   name = models.CharField(max_length=100)
   email = models.CharField(max_length=120)

   def __str__(self):
      return self.name
        
    
 
