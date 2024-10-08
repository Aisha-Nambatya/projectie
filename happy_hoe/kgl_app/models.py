from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError
from django.db import models



# Create your models here.
class Stockx(models.Model):
    
    item_name=models.CharField(max_length=50, null = True, blank=True)
    stock_branch_name=models.CharField(max_length=50, null = True, blank=True)
    stock_type=models.CharField(max_length=50, null = True, blank=True)
    stock_time_of_produce=models.CharField(max_length=50, null = True, blank=True)
    stock_contact=models.CharField(max_length=50, null = True, blank=True)
    stock_source = models.CharField(max_length=50, null = True, blank=True)
    unit_cost = models.IntegerField(default=10, null = True, blank=True)
    unit_price = models.IntegerField(default=0, null = True, blank=True)
    total_quantity = models.IntegerField(default=0, null = True, blank=True)
    issued_quantity = models.IntegerField(default=0, null = True, blank=True)
    def __str__(self):
        return self.item_name

   






class Sales(models.Model):
    branch_name = models.CharField(max_length=100, null=True, blank=True)
    item = models.ForeignKey(Stockx, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=10, null=True, blank=True)
    amount_received = models.IntegerField(default=10, null=True, blank=True)
    issued_to = models.CharField(max_length=50, null=True, blank=True)
    unit_price = models.IntegerField(default=10, null=True, blank=True)
    date = models.DateField(default=datetime.now)
    
    # Adding time field
    time = models.TimeField(default=datetime.now, null=True, blank=True)


#defining a method

    def get_total(self):
        total = self.quantity * self.item.unit_price
        return int(total)


    def get_change(self):
        change = self.get_total() - self.amount_received
        return abs(int(change))
    

    def __str__(self):
        return self.item.item_name


class Deffered_payments(models.Model):
    customer_name = models.CharField(max_length=50, null=True, blank=True)
    contact = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    nin = models.CharField(max_length=50, null=True, blank=True, unique=True)
    item_bought_on_credit = models.CharField(max_length=50, null=True, blank=True)
    amount = models.IntegerField(default=0, null=True, blank=True)
    balance = models.IntegerField(default=0, null=True, blank=True)
    date = models.DateField(default=datetime.now)
    date_of_payment = models.DateField(default=datetime.now)
    branch = models.CharField(max_length=50, null=True, blank=True)
    agent = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.customer_name) 


    def clean(self):
        # Example: Check if the NIN is valid
        if not self.nin:
            raise ValidationError('NIN is required.')

        