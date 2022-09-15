from django.db import models

class Customer(models.Model):
    user_name = models.CharField(max_length=30)  # should have relational stuff and cascade and everything 
    email_id = models.EmailField(max_length=30)
    password = models.CharField(max_length=30) # should be hashed 
    gender = models.CharField(max_length=10) # should have choices insted of string
    date_of_birth = models.DateField()
    contact_number = models.IntegerField() # is integerfield the right choice ?
    role = models.CharField(max_length=10) # should be enum values with admin, user options
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()