from django.db import models

class UserInfo(models.Model):
    first_name = models.CharField(max_length=100,blank=True, null=True)
    last_name = models.CharField(max_length=100,blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=100,blank=True, null=True)
    street_address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100)
    county = models.CharField(max_length=100, blank=True, null=True)
    postcode = models.CharField(max_length=20,blank=True, null=True)
    phone = models.CharField(max_length=20,blank=True, null=True)
    email = models.EmailField(unique=True,blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

class Order(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name="orders")
    order_id = models.CharField(max_length=50, unique=True)
    quantity = models.IntegerField()
    total_entries = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    crypto_currency = models.CharField(max_length=10)
    crypto_amount = models.DecimalField(max_digits=10, decimal_places=5)
    fiat_currency = models.CharField(max_length=10)
    fiat_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_and_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.order_id} - {self.user.email}"
