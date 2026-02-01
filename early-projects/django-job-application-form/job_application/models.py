from django.db import models

class Form(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()  # ❌ remove unique=True
    phone = models.CharField(max_length=20)
    occupation = models.CharField(max_length=50)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
