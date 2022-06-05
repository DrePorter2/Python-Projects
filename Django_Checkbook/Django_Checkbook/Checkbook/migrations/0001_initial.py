# Generated by Django 4.0.4 on 2022-06-04 01:10

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('initial_deposit', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
            managers=[
                ('Accounts', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('type', models.CharField(choices=[('Deposit', 'Deposit'), ('Withdrawal', 'Withdrawal')], max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('description', models.CharField(max_length=500)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Checkbook.account')),
            ],
            managers=[
                ('Transaction', django.db.models.manager.Manager()),
            ],
        ),
    ]
