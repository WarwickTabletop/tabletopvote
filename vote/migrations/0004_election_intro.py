# Generated by Django 3.1.3 on 2020-11-16 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0003_auto_20201116_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='election',
            name='intro',
            field=models.TextField(blank=True, help_text='The text to display at the top of the election. HTML enabled'),
        ),
    ]