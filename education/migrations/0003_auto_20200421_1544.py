# Generated by Django 3.0.4 on 2020-04-21 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_auto_20200413_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educationpost',
            name='image',
            field=models.ImageField(default='/static/images/postdefault.jpg', upload_to='images/'),
        ),
    ]
