# Generated by Django 3.2.5 on 2021-08-11 01:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movie', '0002_auto_20210811_1006'),
        ('review', '0002_auto_20210809_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='review',
            name='like_review',
        ),
        migrations.AddField(
            model_name='review',
            name='like_review',
            field=models.ManyToManyField(default=0, related_name='like_review', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='movie.movie'),
        ),
        migrations.RemoveField(
            model_name='review',
            name='unlike_review',
        ),
        migrations.AddField(
            model_name='review',
            name='unlike_review',
            field=models.ManyToManyField(default=0, related_name='unlike_review', to=settings.AUTH_USER_MODEL),
        ),
    ]