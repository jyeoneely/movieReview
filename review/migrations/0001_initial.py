# Generated by Django 3.2.5 on 2021-08-06 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.CharField(max_length=50)),
                ('star', models.PositiveIntegerField()),
                ('author', models.CharField(max_length=10)),
                ('create_date', models.DateTimeField()),
                ('modify_date', models.DateTimeField(blank=True, null=True)),
                ('content', models.TextField()),
                ('like_review', models.IntegerField(default=0)),
                ('unlike_review', models.IntegerField(default=0)),
                ('review_hit', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
