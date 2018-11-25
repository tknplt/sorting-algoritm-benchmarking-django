"""
  Debug file 
"""

def dd(arr):
    """
        Debug array print 
        :param arr: list of arr 
        :return: void
    """
    print('Ekrana Basılıyor... OK')
    n = len(arr)
    for i in range(n): 
        print("{:7d} - {}".format(i, arr[i]))

    print('Ekrana Basma Bitti... OK')