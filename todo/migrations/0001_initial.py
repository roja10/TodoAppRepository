# Generated by Django 3.0.6 on 2020-10-23 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=1000)),
                ('description', models.TextField()),
                ('completed', models.BooleanField(default=True)),
            ],
        ),
    ]