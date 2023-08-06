from django.db import models

# Create your models here.
class BookStoreModel(models.Model):
    CATEGORY = (
        ('Mystery', 'Mystery'),
        ('Thriller','Thriller'),
        ('Sci-Fi', 'Si-Fi'),
        ('Humor','Humor'),
        ('Horror','Horror'),
    )
    id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    category = models.CharField(max_length=30, choices=CATEGORY)
    first_pub = models.DateTimeField(auto_now_add=True) # first date will show
    last_pub = models.DateTimeField(auto_now=True) # then when we update it will change
