# Generated by Django 3.0.8 on 2021-01-16 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preparation', '0003_register_branch'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addquestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=4000)),
                ('answer', models.CharField(max_length=5000)),
            ],
        ),
    ]