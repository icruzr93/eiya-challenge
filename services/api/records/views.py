from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Record
from .serializers import RecordSerializer
from .tasks import calc_fibonacci


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_record(request, pk):
    try:
        record = Record.objects.get(pk=pk)
    except Record.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RecordSerializer(record)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = RecordSerializer(record, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def get_post_records(request):

    if request.method == 'GET':
        records = Record.objects.all().order_by('-id')
        serializer = RecordSerializer(records, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = {
            'number': request.data.get('number'),
            'state': 'PENDING'
        }
        serializer = RecordSerializer(data=data)
        if serializer.is_valid():
            record = serializer.save()
            calc_fibonacci.delay(record.id, record.number)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
