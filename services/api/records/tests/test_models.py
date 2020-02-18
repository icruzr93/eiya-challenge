from django.test import TestCase
from ..models import Record


class RecordTest(TestCase):
    """ Test module for Record model """

    def setUp(self):
        Record.objects.create(number=3, state='PENDING')
        Record.objects.create(number=20, state='PENDING'),
        Record.objects.create(number=30, state='PENDING'),
        Record.objects.create(number=7, state='PENDING')

    def test_record(self):
        record1 = Record.objects.get(number='3')
        self.assertEqual(record1.get_state(), "3 has the state: PENDING")
        record2 = Record.objects.get(number='20')
        self.assertEqual(record2.get_state(), "20 has the state: PENDING")
        record3 = Record.objects.get(number='30')
        self.assertEqual(record3.get_state(), "30 has the state: PENDING")
        record4 = Record.objects.get(number='7')
        self.assertEqual(record4.get_state(), "7 has the state: PENDING")
