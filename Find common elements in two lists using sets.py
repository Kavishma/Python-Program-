# Find common elements in two lists using sets

n = int(input("no of elements in set1:"))
set1 = set()
for i in range(1, n + 1):
    d = int(input("enter %d element:" % i))
    set1.add(d)

n = int(input("\nno of elements in set2:"))
set2 = set()
for i in range(1, n + 1):
    d = int(input("enter %d element:" % i))
    set2.add(d)

result_list = list(set1.intersection(set2))
print(result_list)

