# Generated by Django 4.1.2 on 2023-03-27 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
