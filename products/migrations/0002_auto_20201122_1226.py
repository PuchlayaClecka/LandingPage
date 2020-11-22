# Generated by Django 3.1.3 on 2020-11-22 09:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='article_number',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='box_size',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('9cf74b10-5e9f-4e6d-93e7-c1714ccb01c8'), editable=False),
        ),
    ]
