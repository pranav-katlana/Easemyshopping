# Generated by Django 3.1.7 on 2021-03-29 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=122)),
                ('Brand', models.CharField(max_length=122)),
                ('category', models.CharField(max_length=122)),
                ('img1', models.CharField(max_length=2600)),
                ('img2', models.CharField(max_length=2600)),
                ('img3', models.CharField(max_length=2600)),
                ('Description', models.CharField(max_length=2000)),
                ('GSM', models.IntegerField(max_length=2)),
                ('kyg', models.IntegerField(max_length=2)),
                ('gadgets', models.IntegerField(max_length=2)),
                ('youtube', models.CharField(max_length=2600)),
                ('Amazon_Link', models.CharField(max_length=3000)),
                ('Flipkart_Link', models.CharField(max_length=3000)),
            ],
        ),
    ]
