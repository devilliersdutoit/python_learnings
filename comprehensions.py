some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# list only the duplicates

dup_list = list(set([x for x in some_list if some_list.count(x) > 1]))
dup_list.sort()
print(dup_list)
