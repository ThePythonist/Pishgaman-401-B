def newsort(lst):
    lst.sort()
    return lst[::-1]


numbers = [3, 14, 2, 7, 5, 1]
print(newsort(numbers))
