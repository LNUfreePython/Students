#SortBubble
def SortBubble(sort):
    length = len(sort)
    for i in range(0, length):
        for j in range(0, length - i - 1):
            if sort[j] > sort[j + 1]:
                temp = sort[j]
                sort[j] = sort[j + 1]
                sort[j + 1] = temp

print("Sort Bubble")
number = []
n = int(input("type lenght of massif: ")) 
for i in range(0, n): 
    element = int(input("number[" + str(i + 1) + "] = "))   
    number.append(element)
SortBubble(number) 
print("sorted massif: ") 
print(number)



#Сортування вставкою
def SortInsertion(sort): 
    length = len(sort) 
    for i in range(1, length):
        key = sort[i]
        j = i
        while (j - 1 >= 0) and (sort[j - 1] > key):
            sort[j - 1], sort[j] = sort[j], [j - 1]
            j = j - 1
        sort[j] = key

print("Sort insert")
number = []
length = int(input("type lenght of massif: ")) 
for i in range(0, length): 
    element = int(input("number[" + str(i + 1) + "] = "))   
    number.append(element)
SortInsertion(number) 
print("sorted massif: ") 
print(number)



#Сортування вибором
def SortSelection():
    lis_1 = [1,2,3,4,5]
    list_1 = a
    length = len(a)
    for i in range(length -1):
        k = a[i]
        f = i
        for j in range (i+1, length):
            if k > a[j]:
                k = a[j]
                f = j 

        if f !=i:
            t = a[i]
            a[i]=a[f]
            a[f]=t
print (a)


