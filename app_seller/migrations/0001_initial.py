# Generated by Django 4.1 on 2022-09-13 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userseller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('pic', models.FileField(default='anonymous.png', upload_to='buyer_images')),
            ],
        ),
    ]