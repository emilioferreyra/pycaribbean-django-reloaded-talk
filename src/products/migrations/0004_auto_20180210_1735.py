# Generated by Django 2.0.2 on 2018-02-10 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20180210_1648'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='make',
            name='product_type',
        ),
        migrations.AddField(
            model_name='model',
            name='product_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='products.ProductType'),
        ),
    ]
