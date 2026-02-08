import random
count = int(input('Enter a number of elements that you want in your array :'))

n = 0

def randarray(count):
    x = []

    for i in range(count + 1):
        x.append(random.randint(-1000, 1000))

    return x 

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

def bubble_sort(arr): # O(n^2)
    global n
    for j in range(0, len(arr)-1):
        changed = False
        for i in range(0, len(arr)-1):
            n += 1
            if arr[i] > arr[i+1]:
                swap(arr, i, i+1)
                changed = True
                
        if not changed:
            break
        
    return arr

def selection_sort(arr):
    global n

    for i in range(len(arr)):
        min_index = i
        
        for j in range(i+1, len(arr)):
            n +=1
            if arr[j] < arr[min_index]:
                min_index = j
        
        swap(arr, i, min_index)

    return arr

def insert_sort_misha(arr):
    global n

    insert_array = [arr[0]]

    for i in range(1, len(arr)):  # O(n)
        inserted = False

        for j in range(len(insert_array)):  # O(n)
            n += 1
            if arr[i] < insert_array[j]:
                insert_array.insert(j, arr[i]) # O(n)
                inserted = True
                break

        if not inserted:
            insert_array.append(arr[i]) # O(n)

    return insert_array

def insert_sort(arr):
    global n

    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            n += 1
            swap(arr, j, j - 1)
            j -= 1

    return arr                


def fact_iteractive(x):
    result = 1
    for i in range(2, x):
        result = result * i

    return result

def fact(x):
    if x == 1:
        return 1
        
    return x * fact(x-1)


def merge_sort(arr):     # O(n*lgn)
    global n
    n += 1

    if len(arr) <= 1:
        return arr
    
    middle = len(arr) // 2
    left_half = merge_sort(arr[:middle])
    right_half = merge_sort(arr[middle:])
    
    return merge(left_half, right_half)

def merge(left, right):
    global n

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        n += 1 
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    n += len(left[i:])
    result.extend(right[j:])
    n += len(right[j:])

    return result


def quick_sort_by_gpt(array):   # O(3n*lg(n))
    global n
    n += 1
    
    if len(array) <= 1:
        return array
    else:
        main = array[len(array) // 2] 

        left = []
        for x in array:  # O(n)
            n += 1
            if x < main:
                left.append(x)
                
        middle = []
        for x in array:  # O(n)
            n += 1
            if x == main:
                middle.append(x)
                
        right = []
        for x in array:  # O(n)
            n += 1
            if x > main:
                right.append(x)
                
        return quick_sort(left) + middle + quick_sort(right)     

def _quick_sort(array):
    global n
    n += 1

    if len(array) <= 1:
        return array
    else:
        p = len(array) - 1
        i = 0
        j = p - 1
        pivot = array[p]
        while j > i:
            n += 1
            if array[i] <= pivot:
                i += 1
            elif array[j] > pivot:
                j -= 1
            else:
                swap(array, i, j)
                j -= 1
                i += 1

        if array[i] <= pivot:
            i += 1
        swap(array, i, p)
        
    return _quick_sort(array[:i]) + [pivot] + _quick_sort(array[(i+1):])    


def quick_sort(array, start, end):
    global n
    n += 1

    if end - start < 1:
        return array
    else:
        p = end
        i = start
        j = p - 1
        pivot = array[p]
        while j > i:
            n += 1
            if array[i] <= pivot:
                i += 1
            elif array[j] > pivot:
                j -= 1
            else:
                swap(array, i, j)
                j -= 1
                i += 1

        if array[i] <= pivot:
            i += 1
        swap(array, i, p)

    
    quick_sort(array, start, i - 1)
    quick_sort(array, i + 1, end)

    return array   

def is_sorted(array):
    m = -99999999999999999999
    for el in array:
        if el < m:
            return False
        m = el
    return True

array = randarray(count)
# print(array)   
print('========')

print(array)

print('-----')

# array = bubble_sort(array) # 10000

# array = selection_sort(array)  # 5050

# array = insert_sort(array)  # 2800

# array = merge_sort(array) # 881

array = quick_sort(array, 0, len(array) - 1)

print(array)
print(is_sorted(array))


# print(f"It tooks that many operations: {n}")
# n = 0

def search(array, number):
    global n
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = (left+right) // 2
        n += 1
        if array[middle] == number:
            return middle  
        elif array[middle] < number:
            left = middle + 1  
        else:
            right = middle - 1  

    return -1

# num = int(input('Ведите число которое хотите найти :'))
# finding_index = search(array, num)
# print(f'Я нашел ваше число в ячейке {finding_index}, если я вывел число -1 значит вашего числа нет в этом масиве')
# print(f"It tooks that many operations: {n}")
