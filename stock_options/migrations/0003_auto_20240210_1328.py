# Generated by Django 3.2.13 on 2024-02-10 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_options', '0002_auto_20240210_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='average_price',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=5),
        ),
        migrations.AlterField(
            model_name='stockitem',
            name='kind',
            field=models.CharField(choices=[('stock', 'Stock'), ('put', 'Put'), ('call', 'Call')], default='stock', max_length=200),
        ),
    ]
