from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    release_date = models.DateField(default=None)
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(default=None)

    def __str__(self):
        return f'{self.name}, {self.price}: {self.release_date}'
