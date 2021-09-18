from django.db import models


# Create your models here.
class ApiExchange(models.Model):
    date = models.DateField(unique=True)
    rate_eur_rur = models.DecimalField(decimal_places = 14, max_digits = 40)
    rate_usd_rur = models.DecimalField(decimal_places = 14, max_digits = 40)


class CatPhoto(models.Model):
    photo = models.ImageField(upload_to='cat_photos')

    class Meta:
        verbose_name_plural = "Cat photos"

    def __str__(self):
        return self.photo.name
