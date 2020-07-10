def bubbleSort(list):
    tmp = 0
    count = 0
    length = len(list)
    for i in range(length):
        idx = 0
        for j in range(length - 1):
            # print('count : {}'.format(count))
            print('list: {}'.format(list))
            if list[idx] > list[idx + 1]:
                tmp = list[idx]
                list[idx] = list[idx + 1]
                list[idx + 1] = tmp
            idx += 1
            count += 1
        idx = 0
    return list
list = [5, 3, 5, 2]
print(bubbleSort(list))