from django.db import models

# Create your models here
  
class customer(models.Model):
    name = models.CharField(max_length=200,null=True)
    age= models.IntegerField()
    email = models.CharField(max_length=200,null=True)
    phone = models.IntegerField(max_length=200,null=True)
    aadhaar= models.IntegerField()
    password = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name  


class staff(models.Model):
    name = models.CharField(max_length=200,null=True)
    age= models.IntegerField()
    email = models.CharField(max_length=200,null=True)
    phone = models.IntegerField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True)
    aadhaar= models.IntegerField()
    loginapproval=models.BooleanField(default=False)
    
    def __str__(self):
        return self.name     


class Room(models.Model):
    AVAILABILITY_CHOICES = (
        ('available', 'Available'),
        ('not_available', 'Not Available'),
    )

    ROOM_TYPE_CHOICES = (
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite'),
    )

    room_number = models.CharField(max_length=50, unique=True)
    room_type = models.CharField(max_length=100, choices=ROOM_TYPE_CHOICES)
    capacity = models.PositiveIntegerField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='available')

    def __str__(self):
        return self.room_number
    
class Booking(models.Model):
    customer = models.ForeignKey(customer,on_delete=models.SET_NULL,related_name= 'cust',null=True) 
    room = models.ForeignKey(Room, on_delete=models.SET_NULL,related_name= 'room',null=True) 
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    approval=models.BooleanField(default=False)

    def __str__(self):
        return self.customer.name