from django.db import models

class Property(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    owner = models.CharField(max_length=255)
    number_of_units = models.IntegerField()

    def __str__(self):
        return self.name

class Tenant(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    rented_property = models.ForeignKey(Property, on_delete=models.CASCADE)
    move_in_date = models.DateField()
    rent_due_date = models.DateField()

    def __str__(self):
        return self.name

class Payment(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.tenant.name} - {self.amount}"
