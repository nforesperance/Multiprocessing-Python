from multiprocessing import Pool
import multiprocessing as mp
import pprint
pp = pprint.PrettyPrinter(indent=4, width=41, compact=True)
import json
import requests


def dispatcher(request):
    urls = [
        ['https://jsonplaceholder.typicode.com/todos/2', 1],
        ['http://jsonplaceholder.typicode.com/users/2', 2],
        ['http://jsonplaceholder.typicode.com/users/2', 3]
    ]
    return urls


def requests_handler(arr):
    url = arr[0]
    if arr[1] == 1:
        response = requests.get(url)
        return response.json()
    elif arr[1] == 2:
        response = requests.get(url)
        return response.json()
    elif arr[1] == 3:
        response = requests.get(url)
        return response.json()


def reconciler(pool, request):
    return pool.map(requests_handler, dispatcher(request))


if __name__ == '__main__':
    pool = mp.Pool(mp.cpu_count())
    responses = reconciler(pool, 'request')
    print('\n')
    pp.pprint(responses)
    print('\n')
    pool.close()
    # print(responses)
