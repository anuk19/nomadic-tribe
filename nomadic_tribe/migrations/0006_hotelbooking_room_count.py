# Generated by Django 4.1.5 on 2023-02-10 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0005_amenities_hotel_review_hotel_amenities'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelbooking',
            name='room_count',
            field=models.IntegerField(default=1),
        ),
    ]
