import random
import time
from django.shortcuts import render
from .models import Sorting
from random import randint
from django.http import JsonResponse
from datetime import datetime
from django.db.models import Avg

from helper.shellsort import shellSort, _random_string
from helper.radixsort import _radixSort
from helper.mergesort import _mergeSort
from helper.mergesortparalel import merge_sort, merge_sort_parallel
from helper.countsort import _countSort
from helper.quicksort import _quickSort
from helper.debug import dd

def shellshortprinter(request):
    result = Sorting.objects.filter(sorting_type='shellsort').values('data_type').annotate(expired=Avg('expired_time'))
    print(result)
    data = []
    for row in result:
        data.append([row['data_type'], row['expired']])

    return JsonResponse({'data':data})


#merge sort parelel

def mergesort_paralel(request):
    context = {
        'action':'mergesort_paralel_execute',
        'result':Sorting.objects.filter(sorting_type='mergesort_paralel').
                    values('expired_time', 'batch_size', 'data_type', 'create_at').order_by('-id')
    }
    return render(request, 'sorting/sorting.html', context)

def mergesort_paralel_execute(request):
    batch_size = int(request.POST.get('batch_size', None))
    data_type = request.POST.get('data_type', None)

    if data_type == 'int':
        arr = [randint(0, 100000) for i in range(batch_size)]
    elif data_type == 'float':
        arr = [random.random() for i in range(batch_size)]
    elif data_type == 'string':
        arr = [_random_string() for i in range(batch_size)]
    

    index = 1
    for sort in merge_sort, merge_sort_parallel: 
        startfor = time.time()
        data_sorted = sort(arr)
        endfor = time.time() - startfor
        sorting_type = 'mergesort' if index == 1 else 'mergesort_paralel'
        index += 1
        ekle = Sorting(expired_time=endfor, batch_size=batch_size, data_type=data_type, 
                    sorting_type=sorting_type, create_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        ekle.save()
        print (sort.__name__, endfor, sorted(arr) == data_sorted)
    dd(sort(arr))
    return JsonResponse({'status':True, 'time':endfor})

def shellsort(request):
    context = {
        'action':'sorting_execute',
        'sort_type':'shellsort',
        'int_status' : True,
        'float_status' : True,
        'string_status' : True,
        'result':Sorting.objects.filter(sorting_type='shellsort')
            .values('expired_time', 'batch_size', 'data_type', 'create_at').order_by('-id')
    }
    return render(request, 'sorting/sorting.html', context)

#radix sort 
def radixsort(request):
    context = {
        'action':'sorting_execute',
        'sort_type':'radixsort',
        'int_status' : True,
        'float_status' : True,
        'string_status' : True,
        'result':Sorting.objects.filter(sorting_type='radixsort').values('id', 'expired_time', 'batch_size', 'data_type', 'create_at').order_by('-id')
    }
    return render(request, 'sorting/sorting.html', context)


#count sort
def countsort(request):
    context = {
        'action':'sorting_execute',
        'sort_type':'countsort',
        'int_status' : True,
        'float_status' : False,
        'string_status' : False,
        'result':Sorting.objects.filter(sorting_type='countsort').values('id','expired_time', 'batch_size', 'data_type', 'create_at')
    }
    return render(request, 'sorting/sorting.html', context)


#quick sort
def quicksort(request):
    context = {
        'action':'sorting_execute',
        'sort_type':'quicksort',
        'int_status' : True,
        'float_status' : True,
        'string_status' : True,
        'result':Sorting.objects.filter(sorting_type='quicksort').values('id','expired_time', 'batch_size', 'data_type', 'create_at')
    }
    return render(request, 'sorting/sorting.html', context)

def sorting_execute(request):
    batch_size = int(request.POST.get('batch_size', None))
    data_type = request.POST.get('data_type', None)
    sort_type = request.POST.get('sort_type', None)
    if data_type == 'int':
        arr = [randint(0, 10000001) for i in range(batch_size)]
    elif data_type == 'float':
        arr = [random.random() for i in range(batch_size)]
    elif data_type == 'string':
        arr = [_random_string() for i in range(batch_size)]

    start = time.time()
    if sort_type == 'quicksort':            
        _quickSort(arr,0,batch_size-1)
    elif sort_type == 'countsort':
        arr = _countSort(arr, max(arr))
    elif sort_type == 'radixsort':
        _radixSort(arr)
    elif sort_type == 'shellsory':
        shellSort(arr)
    end = time.time() - start

    dd(arr)
    
    ekle = Sorting(expired_time=end, batch_size=batch_size, data_type=data_type, 
                    sorting_type=sort_type, create_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    ekle.save()
    return JsonResponse({'status':True, 'time':end, 'id':ekle.id})