import collections

lis = [10, 20, 30, 40, 50]
print(list(enumerate(lis)))  # [(0, 10), (1, 20), (2, 30), (3, 40), (4, 50)]
dict = collections.defaultdict(list)
for index, value in enumerate(lis):
    dict[value].append(index)
#print(dict)  # defaultdict(<class 'list'>, {10: [0], 20: [1], 30: [2], 40: [3], 50: [4]})
#print(dict.keys())
#print(list(dict.keys()))
#print(list(dict.keys())[0])
dict2 = {'asas': [0], 'asaaaa': [1]}
print(len(dict2))

