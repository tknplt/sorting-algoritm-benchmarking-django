from django.urls import path
from . import views
app_name = 'sorting'

urlpatterns = [
    path('shellsort', views.shellsort, name='shellsort'),
    path('shellshortprinter', views.shellshortprinter, name='shellshortprinter'),

    path('radixsort', views.radixsort, name='radixsort'),


    path('mergesort_paralel', views.mergesort_paralel, name='mergesort_paralel'),
    path('mergesort_paralel_execute', views.mergesort_paralel_execute, name='mergesort_paralel_execute'),

    path('countsort', views.countsort, name='countsort'),
    path('quicksort', views.quicksort, name='quicksort'),
    path('selectionsort', views.selectionsort, name='selectionsort'),



    #ortak
    path('sorting_execute', views.sorting_execute, name='sorting_execute'),
]