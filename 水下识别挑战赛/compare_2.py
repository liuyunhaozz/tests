from collections import Counter


with open('fp16.csv', 'r') as f:
    lst_1 = f.readlines()
with open('testBf.csv', 'r') as f:
    lst_2 = f.readlines()

lst_1 = Counter(lst_1)
lst_2 = Counter(lst_2)

print (dict(lst_1)==dict(lst_2))
