# Generated by Django 3.0.7 on 2020-07-30 03:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('eid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('upvote_count', models.PositiveIntegerField(default=0)),
                ('downvote_count', models.PositiveIntegerField(default=0)),
                ('title', models.CharField(max_length=200)),
                ('url', models.URLField(blank=True, null=True, verbose_name='URL')),
                ('text', models.TextField(blank=True, null=True)),
                ('comment_count', models.PositiveIntegerField(default=0)),
                ('submitter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts_submitted', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SubReddit',
            fields=[
                ('eid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('name', models.CharField(max_length=200)),
                ('cover_image_url', models.URLField(blank=True, null=True, verbose_name='Cover Image URL')),
                ('moderators', models.ManyToManyField(related_name='subreddits_moderated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SubRedditPost',
            fields=[
                ('eid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subreddits_set', to='reddit.Post')),
                ('subreddit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts_set', to='reddit.SubReddit')),
            ],
            options={
                'unique_together': {('subreddit', 'post')},
            },
        ),
        migrations.AddField(
            model_name='subreddit',
            name='posts',
            field=models.ManyToManyField(blank=True, related_name='subreddits', through='reddit.SubRedditPost', to='reddit.Post'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('eid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('upvote_count', models.PositiveIntegerField(default=0)),
                ('downvote_count', models.PositiveIntegerField(default=0)),
                ('text', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_authored', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='reddit.Comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='reddit.Post')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserVote',
            fields=[
                ('eid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('object_id', models.UUIDField()),
                ('vote_type', models.CharField(choices=[('U', 'Up Vote'), ('D', 'Down Vote')], max_length=1)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('voter', 'object_id', 'content_type')},
            },
        ),
    ]