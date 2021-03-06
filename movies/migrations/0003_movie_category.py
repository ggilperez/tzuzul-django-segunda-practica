# Generated by Django 3.2.9 on 2021-12-05 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_remove_category_movies'),
        ('movies', '0002_alter_movie_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movies', to='categories.category'),
        ),
    ]
