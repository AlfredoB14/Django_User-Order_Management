# Generated by Django 5.0.4 on 2024-05-07 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('batch', '0016_alter_batch_flavour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='boxes',
            field=models.IntegerField(choices=[(5, 'Small (5)'), (10, 'Medium (10)'), (15, 'Big (15)')], default=None),
        ),
        migrations.AlterField(
            model_name='batch',
            name='units_per_box',
            field=models.IntegerField(choices=[(5, 'Small (5)'), (10, 'Medium (10)'), (15, 'Big (15)')], default=None),
        ),
    ]
