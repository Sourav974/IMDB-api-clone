# Generated by Django 4.0.3 on 2022-04-07 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0007_review_avg_rating_review_number_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='active',
            field=models.BooleanField(default=0),
        ),
    ]
