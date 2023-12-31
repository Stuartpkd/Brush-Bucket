# Generated by Django 3.2.22 on 2023-11-20 13:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('brushes', '0003_rating'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavedBrush',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brush', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='savedbrush_set', to='brushes.brush')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
