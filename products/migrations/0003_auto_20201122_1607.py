# Generated by Django 3.1.3 on 2020-11-22 13:07

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20201122_1226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.UUID('cb2dfd05-ebbc-4b4e-a4cd-0da79500db31'), editable=False)),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='article_number',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='box_size',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('662d55db-65b5-46ae-bab3-601470be961b'), editable=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='for_age',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.ages'),
        ),
    ]
