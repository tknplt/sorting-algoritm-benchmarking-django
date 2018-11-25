from django.db import models

class Sorting(models.Model):
    expired_time = models.FloatField()
    batch_size = models.IntegerField()
    data_type = models.CharField(max_length=15)
    sorting_type = models.CharField(max_length=20)
    create_at = models.DateTimeField()

    def __str__(self):
        return '{}, {}, {}, {}'.format(__class__, self.batch_size, self.expired_time, self.sorting_type)

    class Meta:
        db_table = 'sorting_result'
        ordering = ['-id']
