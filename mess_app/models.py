from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(
        verbose_name="Name",
        max_length=254,
        help_text="(e.g. 'Anna' or 'Anna-Claire')",
    )

    last_name = models.CharField(
        verbose_name="Surname",
        max_length=254,
        help_text="(e.g. 'Stopford' or 'Stopford-Sackville')",
    )

    email = models.EmailField(
        max_length=254,
        unique=True,
        help_text="(A valid email address, please.)",
    )

    class Meta:
        ordering = ['last_name', 'first_name', 'email']

    def __str__(self):
        return f"{self.first_name}_{self.last_name}({self.email})"
