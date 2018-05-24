from django.db import models
from django.utils import timezone
# Create your models here.
class Entry(models.Model):
    amount = models.DecimalField(max_digits=6,decimal_places=2)
    description = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    type = models.CharField(default="expense",max_length=40)

    @property
    def get_amount(self):
        return "R$" + str(self.amount)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = "entries"
