#find duplicate sets in a list using set

from collections import counter
test_list=[{1,2,3,4},{4,5},{1,2},{4,5},{23},{1,2},{23}]
print("the list\n"+str(test_list))
frqs=counter(frozenset(sub) for sub in test_list)
if len(frqs)>0:
    print("\nduplicate set list:")
    for key,val in frqs.items():
        if val>1:
            print(key) 
