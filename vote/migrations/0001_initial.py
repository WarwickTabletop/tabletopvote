# Generated by Django 3.1.3 on 2020-11-14 00:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Election',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('max_votes', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('text', models.TextField()),
                ('election', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.election')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
                ('election', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.election')),
            ],
            options={
                'unique_together': {('ip', 'election')},
            },
        ),
    ]