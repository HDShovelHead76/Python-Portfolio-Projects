from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

MEAL_TYPE = (
    ("starters", "Starters"),
    ("salads", "Salads"),
    ("main_dishes", "Main Dishes"),
    ("deserts", "Deserts")
)

STATUS = (
    (0, "Unavailable"),
    (1, "Available")
)

class Item(models.Model):
    meal = models.CharField(max_length=500, unique=True)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    category = models.CharField(max_length=500, choices=MEAL_TYPE)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.IntegerField(choices=STATUS, default=1)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.meal)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.meal
