# Generated by Django 2.1.3 on 2019-12-12 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bearing', '0003_auto_20191209_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.BooleanField(default='True'),
        ),
    ]