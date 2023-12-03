from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

