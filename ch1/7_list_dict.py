# List and Dict

tup1 = (1,2,3,[1,2,3],(3,4,5))
tup2 = (10,20,30)
tup_sum = tup1 + tup2
print(tup_sum)
print(tup2*3)

lst1 = [1, 2, 5, 10]
lst2 = [40, 30, 10]
lst1.append(5)
print(lst1)

lst1.pop()
print(lst1)

lst1.pop(0)
print(lst1)

lst1.extend(lst2)
print(lst1)

dct1 = {'a':10,'b':30}

print(list(dct1.keys()))
print(list(dct1.values()))
print(list(dct1.items()))

print(f'tup1[1]:{tup1[1]}, lst1[1]:{lst1[1]}, dct1["a"]:{dct1["a"]}')


