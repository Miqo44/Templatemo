# Generated by Django 4.1.7 on 2023-02-16 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_partner_delete_exp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Info_Name')),
                ('title', models.CharField(max_length=240, verbose_name='title')),
                ('img', models.ImageField(upload_to='', verbose_name='Image')),
                ('bigimg', models.ImageField(upload_to=None, verbose_name='BigImage')),
            ],
        ),
    ]