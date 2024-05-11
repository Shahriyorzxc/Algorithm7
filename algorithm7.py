#Task1
def find_odd(zxc):
    for l in zxc:
        if zxc.count(l) % 2 != 0:
            return l

print(find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5])) # ---> -1
print(find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5])) #---> 5
print(find_odd([10])) # --> 10


#Task2
def filter_listt(w):
    k = []
    for f in w:
        if type(f) == int:
            k.append(f)
    return k


print(filter_listt([1, 2, "a", "b"])) # ---> [1, 2]
print(filter_listt([1, "a", "b", 0, 15])) # ---> [1, 0, 15]
print(filter_listt([1, 2, "aasf", "1", "123", 123])) # ---> [1, 2, 123]


#Task3
lst = [1, 2, 3, 4, 5, 6]
first = 1
middle = [2,3,4,5]
last = 6
print(first) #---> 1
print(middle) #---> [2,3,4,5]
print(last) #---> 6

#Another way
first, *middle, last = [1,2,3,4,5,6]
print(first) #---> 1
print(middle) #---> [2,3,4,5]
print(last) #---> 6


#Task4
def find_even_nums(list1):
    list2 = []
    for x in range(1, list1+1):
        if x % 2 == 0:
            list2.append(x)
    return list2


print(find_even_nums(8)) # ---> [2, 4, 6, 8]
print(find_even_nums(4)) # ---> [2, 4]
print(find_even_nums(2)) # ---> [2]


#Task5
def move_to_end(list, list1):
    for i in range(list.count(list1)):
        list.remove(list1)
        list.append(list1)
    return list


print(move_to_end([1, 3, 2, 4, 4, 1], 1)) # ---> [3, 2, 4, 4, 1, 1]
print(move_to_end([7, 8, 9, 1, 2, 3, 4], 9)) # ---> [7, 8, 1, 2, 3, 4, 9]
print(move_to_end(["a", "a", "a", "b"], "a")) # ---> ["b", "a", "a", "a"]


#Another way
def move_to_end(list, list1):
    for v in list:
        if list1 == v:
           list.remove(list1)
           list.append(list1)
    return list


print(move_to_end([1, 3, 2, 4, 4, 1], 1)) # ---> [3, 2, 4, 4, 1, 1]
print(move_to_end([7, 8, 9, 1, 2, 3, 4], 9)) # ---> [7, 8, 1, 2, 3, 4, 9]
print(move_to_end(["a", "a", "a", "b"], "a")) # ---> ["b", "a", "a", "a"]










