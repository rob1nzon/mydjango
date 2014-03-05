# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True, max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('published', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
