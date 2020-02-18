from celery import shared_task
from datetime import datetime
import requests
import os

from records.models import Record

API_URL = os.environ.get('API_URL')


@shared_task
def fibonacci(n, memo):
    if (n in memo):
        return memo[n]

    if (n < 2):
        return 1

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


@shared_task
def calc_fibonacci(pk, n):
    url = '{0}/records/{1}'.format(API_URL, pk)

    try:
        result = fibonacci(n, {})
        payload = {'result': result, 'state': 'ANALYZED',
                   'analyzed_at': datetime.now()}
    except:
        payload = {'result': 0, 'state': 'ERROR_ANALYZING',
                   'analyzed_at': datetime.now()}

    resp = requests.put(url, data=payload)

    print(resp.status_code)
    print(resp.content)
