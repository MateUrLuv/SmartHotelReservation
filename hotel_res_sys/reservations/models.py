from django.db import models

class Hotel(models.Model):
    hotel_id = models.AutoField(primary_key=True)
    hotel_name = models.CharField(max_length=255, null=False)
    location = models.CharField(max_length=255)
    contact = models.CharField(max_length=20)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    total_rooms = models.IntegerField()

    class Meta:
        db_table = 'hotel'

    def __str__(self):
        return self.hotel_name

class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    hotel_id = models.IntegerField()
    room_number = models.CharField(max_length=10, null=False)
    room_type = models.CharField(max_length=50)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    availability_status = models.BooleanField(default=True)

    class Meta:
        db_table = 'room'

    def __str__(self):
        return f"Room {self.room_number}"

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, unique=True, null=False)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    password = models.CharField(max_length=255, null=False)
    booking_history = models.TextField()

    class Meta:
        db_table = 'customer'

    def __str__(self):
        return self.full_name

class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    room_id = models.IntegerField()
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)

    class Meta:
        db_table = 'reservation'

    def __str__(self):
        return f"Reservation {self.reservation_id}"

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    reservation_id = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=50)
    transaction_date = models.DateField()

    class Meta:
        db_table = 'payment'

    def __str__(self):
        return f"Payment {self.payment_id}"

class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    hotel_id = models.IntegerField()
    full_name = models.CharField(max_length=255, null=False)
    role = models.CharField(max_length=50)
    contact = models.CharField(max_length=20)
    email = models.CharField(max_length=255, unique=True)
    shift_schedule = models.TextField()

    class Meta:
        db_table = 'staff'

    def __str__(self):
        return self.full_name

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    hotel_id = models.IntegerField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    feedback = models.TextField()
    review_date = models.DateField()

    class Meta:
        db_table = 'review'

    def __str__(self):
        return f"Review {self.review_id}"