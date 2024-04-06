from django.db import models
# from django.contrib.auth.models import User
from users.models import User
from rest_framework.authtoken.models import Token


class Width(models.Model):
    title = models.IntegerField()

    def __str__(self):
        return f"{self.title}"


class Profile(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.title}'


class Diameter(models.Model):
    title = models.FloatField()

    def __str__(self):
        return f'{self.title}'


class CarType(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title}'


class Seasonality(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title}'


class Manufacturer(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title}'


class SpeedIndex(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title}'


class LoadIndex(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title}'


class FuelEconomy(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title}'


class GripOnWetSurfaces(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title}'


class LoadIndexForDual(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.title}'


class Model(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.title}'


class ExternalNoiseLevel(models.Model):
    title = models.IntegerField()

    def __str__(self):
        return f'{self.title}'


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title}'


class Tires(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    width = models.ForeignKey('Width', on_delete=models.CASCADE)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    diameter = models.ForeignKey('Diameter', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    promotion = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.IntegerField()
    car_type = models.ForeignKey('CarType', on_delete=models.CASCADE)
    seasonality = models.ForeignKey('Seasonality', on_delete=models.CASCADE)
    state = models.BooleanField(default=False)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.PROTECT)
    discount = models.BooleanField(default=False)
    runflat = models.BooleanField(default=False)
    offroad = models.BooleanField(default=False)
    speed_index = models.ForeignKey('SpeedIndex', on_delete=models.CASCADE)
    load_index = models.ForeignKey('LoadIndex', on_delete=models.CASCADE)
    fuel_economy = models.ForeignKey('FuelEconomy', on_delete=models.CASCADE)
    grip_on_wet_surfaces = models.ForeignKey('GripOnWetSurfaces', on_delete=models.CASCADE)
    external_noise_level = models.ForeignKey('ExternalNoiseLevel', on_delete=models.CASCADE)
    set = models.BooleanField()
    in_stock = models.BooleanField()
    model = models.ForeignKey('Model', on_delete=models.CASCADE)
    load_index_for_dual = models.ForeignKey('LoadIndexForDual', on_delete=models.CASCADE)
    # reviews = models.ForeignKey('Reviews', on_delete=models.CASCADE,  blank=True, null=True)

    def __str__(self):
        return str(self.title)

class Reviews(models.Model):
    tires = models.ForeignKey('Tires', on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(blank=True, null=True)
    rating = models.PositiveIntegerField(choices=((1, '1 star'), (2, '2 star'), (3, '3 star'), (4, '4 star'), (5, '5 star')))

    def __str__(self):
        return f"{self.user}'s - {self.rating} - star rating for {self.tires}"


class Favorite(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tires = models.ForeignKey(Tires, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'tires']

    def __str__(self):
        return f"user: {self.user}, tires: {self.tires}"
