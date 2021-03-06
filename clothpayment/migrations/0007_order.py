# Generated by Django 3.2.5 on 2021-07-16 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clothpayment', '0006_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('shipping_charge', models.IntegerField(default=100)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clothpayment.cart')),
            ],
        ),
    ]
