from tkinter.tix import Tree
from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):

    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Others"),
        ("P", "Preffer Not To Respond"),
    )

    ROLE_CHOICES = (("A", "admin"), ("U", "user"))  # enums

    user_name = models.CharField(max_length=20)  # cascade
    email_id = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)  # hash
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)  # make it optional
    contact_number = models.CharField(max_length=10, blank=True)  # better it
    role = models.CharField(max_length=1, choices=ROLE_CHOICES, default="U", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
