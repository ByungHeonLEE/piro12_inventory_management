# Generated by Django 2.2.9 on 2020-01-26 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='거래처이름')),
                ('telephone', models.CharField(max_length=13, verbose_name='전화번호')),
                ('address', models.CharField(max_length=50, verbose_name='주소')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='상품명')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='제품사진')),
                ('description', models.TextField(blank=True, null=True, verbose_name='상품설명')),
                ('price', models.IntegerField(verbose_name='제품가격')),
                ('left', models.IntegerField(verbose_name='남은수량')),
                ('client', models.CharField(max_length=20, verbose_name='거래처')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='제품등록일')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Client', verbose_name='글쓴이')),
            ],
        ),
    ]
