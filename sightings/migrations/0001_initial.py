import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sighting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('type', models.CharField(max_length=50)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('created_by_id', models.IntegerField(blank=True, null=True)),
                ('created_by_role', models.CharField(blank=True, max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('photo', models.FileField(blank=True, null=True, upload_to='sightings/')),
            ],
        ),
        migrations.CreateModel(
            name='SightingConfirmation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('user_role', models.CharField(max_length=20)),
                ('confirmed_at', models.DateTimeField(auto_now_add=True)),
                ('sighting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='confirmations', to='sightings.sighting')),
            ],
            options={
                'constraints': [models.UniqueConstraint(fields=('sighting', 'user_id'), name='unique_sighting_confirmation')],
            },
        ),
    ]
