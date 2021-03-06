# Generated by Django 2.2.6 on 2019-10-21 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineFood', '0010_addnewcustomer_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerOrder',
            fields=[
                ('Order_id', models.AutoField(primary_key=True, serialize=False)),
                ('Food_Name', models.CharField(max_length=500)),
                ('Food_qty', models.CharField(max_length=500)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('Food_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OnlineFood.AddFood')),
            ],
        ),
    ]
