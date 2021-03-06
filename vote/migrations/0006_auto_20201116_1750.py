# Generated by Django 3.1.3 on 2020-11-16 17:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0005_election_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='vote',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='vote',
            name='ip',
            field=models.GenericIPAddressField(editable=False),
        ),
    ]
