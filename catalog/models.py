"""
1. Реализовать в приложении (catalog созданной в одном из предшествующих заданий) модели использующие
поля OneToOneField, ForeignKey, ManyToManyField.
Пример:
Город
Клиент (MTM на товар, FK на город)
Товар
Поставщик (OTO на город)

"""

from django.db import models  # noqa: F401


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=254)
    state = models.CharField(max_length=254)

    def __str__(self):
        return f"{self.name}/{self.state}"


class Supplier(models.Model):
    title = models.CharField(max_length=254, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    city = models.OneToOneField(
        City,
        on_delete=models.CASCADE,
        primary_key=True
    )

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=254)
    vendor_code = models.CharField(max_length=40)  # vendor_code should be maximum of 40 characters
    exp_date = models.DateField('expiration date')

    def __str__(self):
        return f"{self.title}({self.vendor_code})"


class Client(models.Model):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254, unique=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL,
                             blank=True, null=True,)  # if you delete City, you might want to keep Client
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
