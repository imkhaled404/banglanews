# Generated by Django 3.0.4 on 2020-04-21 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportpost',
            name='image',
            field=models.ImageField(default='/static/images/postdefault.jpg', upload_to='images/'),
        ),
    ]
