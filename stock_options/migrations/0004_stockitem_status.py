# Generated by Django 3.2.13 on 2024-02-10 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_options', '0003_auto_20240210_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockitem',
            name='status',
            field=models.CharField(choices=[('done', 'Done'), ('evaluate', 'Evaluate')], default='done', max_length=200),
        ),
    ]
