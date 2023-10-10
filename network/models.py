from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class Contact(models.Model):
    email = models.EmailField(verbose_name='Почта')
    country = models.CharField(max_length=255, verbose_name='Страна')
    city = models.CharField(max_length=255, verbose_name='Город')
    street = models.CharField(max_length=255, verbose_name='Улица')
    house_number = models.CharField(max_length=10, verbose_name='Номер дома')

    def __str__(self):
        return f'{self.email} / {self.city}'


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Продукт')
    model = models.CharField(max_length=255, verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата выхода')
    manufacturer = models.ForeignKey('NetworkNode', on_delete=models.SET_NULL, verbose_name='Производитель', **NULLABLE)

    def __str__(self):
        return f'{self.name} / {self.model}'


class NetworkNode(models.Model):
    NODE_NAME = (
        ('Завод', 'Завод'),
        ('Розничная сеть', 'Розничная сеть'),
        ('Индивидуальный предприниматель', 'ИП'),
    )

    name = models.CharField(max_length=255, verbose_name='Наименование организации')
    node_type = models.CharField(max_length=50, choices=NODE_NAME, verbose_name='Тип')
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE, verbose_name='Контакты')

    products = models.ManyToManyField(Product, verbose_name='Товары', **NULLABLE)

    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Поставщик', **NULLABLE)
    debt = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Задолженность', **NULLABLE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def product_count(self):
        """ Вывод количества товаров у конкретного поставщика """
        return self.products.count()

    product_count.short_description = 'Количество товаров'

    def get_level(self):
        """ Подсчёт уровня поставщика, завод всегда по умолчанию 0-го уровня """
        if self.node_type == 'Завод':
            return 0
        elif self.supplier:
            return self.supplier.get_level() + 1
        else:
            return 0
    get_level.short_description = 'Уровень поставщика'
