# Generated by Django 4.2 on 2023-04-14 09:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='New Agent', max_length=250)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'agent',
                'verbose_name_plural': 'agents',
            },
        ),
        migrations.CreateModel(
            name='Bot',
            fields=[
                ('agent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='agent.agent')),
            ],
            options={
                'verbose_name': 'bot',
                'verbose_name_plural': 'bots',
            },
            bases=('agent.agent',),
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('agent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='agent.agent')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='avatar', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'avatar',
                'verbose_name_plural': 'avatars',
            },
            bases=('agent.agent',),
        ),
    ]