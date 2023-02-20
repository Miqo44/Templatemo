# Generated by Django 4.1.7 on 2023-02-16 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_hello_bigimg_alter_hello_img_alter_hello_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bigimg', models.ImageField(upload_to=None, verbose_name='BigImage')),
                ('title', models.CharField(max_length=40, verbose_name='title')),
                ('img', models.ImageField(upload_to='', verbose_name='Image')),
                ('subtitle', models.CharField(max_length=200, verbose_name='Begining text')),
                ('first_text', models.TextField(verbose_name='First_Text')),
                ('second_text', models.TextField(verbose_name='Second_Text')),
            ],
        ),
    ]
