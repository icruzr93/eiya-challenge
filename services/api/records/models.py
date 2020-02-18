from django.db import models
from datetime import datetime


class Record(models.Model):
    number = models.IntegerField()
    result = models.BigIntegerField(null=True)
    state = models.CharField(max_length=10)
    created_at = models.DateTimeField(default=datetime.now, null=True)
    analyzed_at = models.DateTimeField(null=True)

    def get_state(self):
        return str(self.number) + ' has the state: ' + self.state

    def _str_(self):
        return self.number
