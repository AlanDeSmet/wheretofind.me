# Generated by Django 2.1.5 on 2019-01-21 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("wheretofindme", "0010_add_initial_aliases")]

    operations = [
        migrations.AddField(
            model_name="user",
            name="search_enabled",
            field=models.BooleanField(default=False),
        )
    ]
