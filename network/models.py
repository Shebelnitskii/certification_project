from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class Contact(models.Model):
    email = models.EmailField()
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=10)


class Product(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    release_date = models.DateField()
    manufacturer = models.ForeignKey('NetworkNode', on_delete=models.SET_NULL, **NULLABLE)


class NetworkNode(models.Model):
    NODE_NAME = (
        ('Завод', 'Завод'),
        ('Розничная сеть', 'Розничная сеть'),
        ('Индивидуальный предприниматель', 'ИП'),
    )

    name = models.CharField(max_length=255)
    node_type = models.CharField(max_length=50, choices=NODE_NAME)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE)

    products = models.ManyToManyField(Product)

    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE)
    debt = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def get_level(self):
        if self.supplier:
            return self.supplier.get_level + 1
        else:
            return 0
