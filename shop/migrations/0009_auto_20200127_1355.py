# Generated by Django 2.2.9 on 2020-01-27 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20200127_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='shop/images', verbose_name='제품사진'),
        ),
    ]
