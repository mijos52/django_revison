# Generated by Django 4.1.1 on 2022-09-15 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_alter_customer_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="date_of_birth",
            field=models.DateField(blank=True, null=True),
        ),
    ]
