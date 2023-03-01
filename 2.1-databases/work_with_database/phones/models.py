from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    image = models.URLField(default='')
    release_date = models.DateField(default=1)
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)
