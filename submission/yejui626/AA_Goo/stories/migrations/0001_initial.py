# Generated by Django 2.2.8 on 2023-06-27 21:50

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('href', models.URLField()),
                ('title', models.CharField(max_length=255)),
                ('comments', models.IntegerField()),
                ('container', jsonfield.fields.JSONField()),
                ('submit_date', models.DateTimeField()),
                ('topic', jsonfield.fields.JSONField()),
                ('promote_date', models.DateTimeField()),
                ('idJSON', models.CharField(max_length=255)),
                ('media', models.CharField(max_length=255)),
                ('diggs', models.IntegerField()),
                ('description', models.TextField()),
                ('link', models.URLField()),
                ('user', jsonfield.fields.JSONField()),
                ('status', models.CharField(max_length=255)),
                ('shorturl', jsonfield.fields.JSONField()),
                ('replica', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Story',
            },
        ),
    ]
