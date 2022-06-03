from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='djangoClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('language', 'language'), ('math', 'math'), ('art', 'art'), ('science', 'science')], max_length=60)),
                ('title', models.CharField(blank=True, default='', max_length=60)),
                ('course_number', models.IntegerField()),
                ('instructor_name', models.CharField(blank=True, default='', max_length=255)),
                ('duration', models.FloatField()),
            ],
        ),
    ]