from django.urls import path
from . import views
app_name = 'sorting'

urlpatterns = [
    path('shellsort', views.shellsort, name='shellsort'),
    path('shellshortprinter', views.shellshortprinter, name='shellshortprinter'),
    path('shellsort_execute', views.shellsort_execute, name='shellsort_execute'),

    path('radixsort', views.radixsort, name='radixsort'),

    path('mergesort', views.mergesort, name='mergesort'),
    path('mergesort_execute', views.mergesort_execute, name='mergesort_execute'),

    path('mergesort_paralel', views.mergesort_paralel, name='mergesort_paralel'),
    path('mergesort_paralel_execute', views.mergesort_paralel_execute, name='mergesort_paralel_execute'),

    path('countsort', views.countsort, name='countsort'),
    path('quicksort', views.quicksort, name='quicksort'),



    #ortak
    path('sorting_execute', views.sorting_execute, name='sorting_execute'),
]