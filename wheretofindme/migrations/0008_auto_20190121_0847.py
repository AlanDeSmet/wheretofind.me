# Generated by Django 2.1.5 on 2019-01-21 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("wheretofindme", "0007_auto_20190112_0001")]

    operations = [
        migrations.AlterModelOptions(
            name="follow",
            options={"ordering": ("to_user__username", "from_user__username")},
        )
    ]