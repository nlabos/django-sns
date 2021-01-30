# Generated by Django 3.1.3 on 2021-01-30 06:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0002_auto_20210119_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='favorite_count',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]