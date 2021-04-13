# Generated by Django 3.2 on 2021-04-08 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_title', models.CharField(max_length=60)),
                ('img_description', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
