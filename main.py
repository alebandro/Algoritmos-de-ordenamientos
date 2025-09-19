from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
#from merge_sort import merge_sort
from selection_sort import selection_sort

lista = [64, 34, 25, 12, 22, 11, 90]

print("Bubble Sort:", bubble_sort(lista.copy()))
print("Insertion Sort:", insertion_sort(lista.copy()))
#print("Merge Sort:", merge_sort(lista.copy()))
print("Selection Sort:", selection_sort(lista.copy()))
