# Generated by Django 2.2.6 on 2019-10-20 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineFood', '0003_auto_20191020_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addnewcustomer',
            name='customer_contact_number',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
