import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Record
from ..serializers import RecordSerializer


client = Client()


class GetAllRecordsTest(TestCase):
    """ Test module for GET all records API """

    def setUp(self):
        Record.objects.create(number=3, state='PENDING')
        Record.objects.create(number=20, state='PENDING'),
        Record.objects.create(number=30, state='PENDING'),
        Record.objects.create(number=7, state='PENDING')

    def test_get_all_records(self):
        response = client.get(reverse('get_post_records'))
        records = Record.objects.all().order_by('-id')
        serializer = RecordSerializer(records, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleRecordTest(TestCase):
    """ Test module for GET single record API """

    def setUp(self):
        self.record1 = Record.objects.create(number=3, state='PENDING')
        self.record2 = Record.objects.create(number=20, state='PENDING'),
        self.record3 = Record.objects.create(number=30, state='PENDING'),
        self.record4 = Record.objects.create(number=7, state='PENDING')

    def test_get_valid_single_record(self):
        response = client.get(
            reverse(
                'get_delete_update_record',
                kwargs={'pk': self.record1.pk}
            )
        )
        record = Record.objects.get(pk=self.record1.pk)
        serializer = RecordSerializer(record)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_record(self):
        response = client.get(
            reverse(
                'get_delete_update_record',
                kwargs={'pk': 30}
            )
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewRecordTest(TestCase):
    """ Test module for inserting a new record """

    def setUp(self):
        self.valid_payload = {
            "number": 2
        }
        self.invalid_payload = {
            "number": "",
        }

    def test_create_valid_record(self):
        response = client.post(
            reverse('get_post_records'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_record(self):
        response = client.post(
            reverse('get_post_records'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleRecordTest(TestCase):
    """ Test module for updating an existing record record """

    def setUp(self):
        self.record1 = Record.objects.create(number=7, state='PENDING')
        self.valid_payload = {
            "number": 30,
        }
        self.invalid_payload = {
            "number": "",
        }

    def test_valid_update_record(self):
        response = client.put(
            reverse(
                'get_delete_update_record',
                kwargs={'pk': self.record1.pk}
            ),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_record(self):
        response = client.put(
            reverse(
                'get_delete_update_record',
                kwargs={'pk': self.record1.pk}
            ),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleRecordTest(TestCase):
    """ Test module for deleting an existing record record """

    def setUp(self):
        self.record1 = Record.objects.create(number=7, state='PENDING')

    def test_valid_delete_record(self):
        response = client.delete(
            reverse('get_delete_update_record', kwargs={'pk': self.record1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_record(self):
        response = client.delete(
            reverse('get_delete_update_record', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
