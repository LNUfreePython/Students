# SortBubble
def bubble_sort(input_array):
    length = len(input_array)
    for i in range(0, length):
        for j in range(0, length - i - 1):
            if input_array[j] > input_array[j + 1]:
                temp = input_array[j]
                input_array[j] = input_array[j + 1]
                input_array[j + 1] = temp
    return input_array

#Сортування вставкою
def insertion_sort(sort): 
    length = len(sort) 
    for i in range(1, length):
        key = sort[i]
        j = i
        while (j - 1 >= 0) and (sort[j - 1] > key):
            sort[j - 1], sort[j] = sort[j], [j - 1]
            j = j - 1
        sort[j] = key

    return sort

# #Сортування вибором
def selection_sort(array):
    size = len(array)
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])

    return array


def print_sorted(array, sorting_type):
  print('Sorted by ' + sorting_type +':')
  if sorting_type == 'bubble':
    print(bubble_sort(array))
  elif sorting_type == 'insert' :
    print(insertion_sort(array))
  elif sorting_type == 'selection':
    print(selection_sort(array), )


random_array = [1,10,3,8,4,14,2,2]
print_sorted(random_array, 'bubble')
print_sorted(random_array, 'insert')
print_sorted(random_array, 'selection')
