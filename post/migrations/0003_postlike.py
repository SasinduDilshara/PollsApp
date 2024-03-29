# Generated by Django 2.2.5 on 2019-10-19 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_delete_postlike'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likedPost', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='post.Post')),
                ('datetime', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
