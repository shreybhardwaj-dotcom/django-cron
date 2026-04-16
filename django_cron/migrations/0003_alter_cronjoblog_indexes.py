# Generated migration to replace index_together with indexes

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_cron', '0002_remove_max_length_from_CronJobLog_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cronjoblog',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='cronjoblog',
            unique_together=set(),
        ),
        migrations.AddIndex(
            model_name='cronjoblog',
            index=models.Index(fields=['code', 'is_success', 'ran_at_time'], name='django_cron_code_is_suc_ran_at_idx'),
        ),
        migrations.AddIndex(
            model_name='cronjoblog',
            index=models.Index(fields=['code', 'start_time', 'ran_at_time'], name='django_cron_code_start_ran_at_idx'),
        ),
        migrations.AddIndex(
            model_name='cronjoblog',
            index=models.Index(fields=['code', 'start_time'], name='django_cron_code_start_idx'),
        ),
    ]
