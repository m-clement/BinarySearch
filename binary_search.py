# Binary search algorithm
def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list) - 1
    steps = 0

    while(start<=end):
        print("Step", steps, ":", str(list[start:end+1])) 

        steps = steps + 1
        middle = (start + end) // 2

        if element == list[middle]:
            return middle
        elif element < list[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return -1

my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17]
target = 11

binary_search(my_list, target)
