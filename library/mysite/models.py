from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 200)
    slug = models.CharField(max_length = 200)
    body = models.TextField()
    release_date = models.TextField()
    
    # class Meta:
    #     ordering = ('-pub_date', )
    # def __str__(self) -> str:
    #     return self.title


# class NewTable(models.Model):
#     bigint_f = models.BigAutoField()
#     bool_f = models.BooleanField()
#     date_f = models.DateField(auto_now = True)
#     char_f = models.CharField(max_length=20, unique = True)
#     datetime_f = models.DateTimeField(auto_now_add = True)
#     decimal_f = models.DecimalField(max_digits = 10, decimal_places = 2)
#     float_f = models.FloatField(null = True)
#     int_f = models.IntegerField(default = 2010)
#     text_f = models.TextField()

class Product(models.Model):
    SIZE = (('S', 'Small'), 
            ('M', 'Medium'),
            ('L', 'Large'),
    )
    sku = models.CharField(max_length=5)
    name = models.CharField(max_length=20)
    price = models.PositiveBigIntegerField()
    size = models.CharField(max_length=1, choices=SIZE)
    result = models.BooleanField()

    def __str__(self):
        return self.name

