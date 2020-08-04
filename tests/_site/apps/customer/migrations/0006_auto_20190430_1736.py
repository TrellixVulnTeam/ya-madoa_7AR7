# Generated by Django 2.0.13 on 2019-04-30 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_auto_20181115_1953'),
    ]

    state_operations = [
        migrations.DeleteModel(
            name='CommunicationEventType',
        ),
        migrations.RemoveField(
            model_name='email',
            name='user',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='recipient',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='sender',
        ),
        migrations.DeleteModel(
            name='Email',
        ),
        migrations.DeleteModel(
            name='Notification',
        ),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=state_operations
        ),
    ]
