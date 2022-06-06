from django.db import models

# Create your models here.
class Feedback(models.Model):
    experience = models.TextField()
    offer = models.TextField()
    price = models.TextField()
    delivery = models.TextField()
    support = models.TextField()
    recommend = models.TextField()
    change = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.email