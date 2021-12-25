# Generated by Django 3.2.9 on 2021-12-02 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('related_customer_name', models.CharField(max_length=100, verbose_name='Customer Name')),
                ('address', models.TextField(verbose_name='Address')),
                ('phone_number', models.CharField(max_length=350, verbose_name='Phone Number')),
            ],
        ),
    ]
