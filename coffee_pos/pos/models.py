from django.db import models

# Create your models here.


from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    table_number = models.IntegerField()
    payment_method = models.CharField(max_length=20)
    total = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()