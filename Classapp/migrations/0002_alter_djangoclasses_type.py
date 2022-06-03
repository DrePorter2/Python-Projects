from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='djangoclasses',
            name='type',
            field=models.CharField(choices=[('language', 'language'), ('art', 'art'), ('science', 'science'), ('math', 'math')], max_length=60),
        ),
    ]