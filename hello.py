def highest_even(li=[]):
    li.sort(reverse=True)
    for item in li:
        if item % 2 == 0:
            return item


my_list = [10, 2, 3, 4, 36, 22, 89, 90, 5,
           6, 11, 24, 77, 34, 5, 6, 7, 8, 9, 10]
print(highest_even(my_list))
