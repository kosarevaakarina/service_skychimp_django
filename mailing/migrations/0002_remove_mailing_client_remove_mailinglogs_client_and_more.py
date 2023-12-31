# Generated by Django 4.2.1 on 2023-06-19 09:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mailing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailing',
            name='client',
        ),
        migrations.RemoveField(
            model_name='mailinglogs',
            name='client',
        ),
        migrations.AddField(
            model_name='mailing',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='активность'),
        ),
        migrations.AddField(
            model_name='mailing',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mailinglogs',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='mailing',
            name='message',
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.AddField(
            model_name='mailing',
            name='message',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mailing.message', verbose_name='Сообщение'),
        ),
    ]
