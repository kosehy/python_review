N = input().split()
row = int(N[0])
col = int(N[1])
# print(row / 2)
door = '.|.'
msg = 'WELCOME'
welcome_pos = int((col - 7) / 2)
center = row // 2

print('welcome_pos : {}'.format(welcome_pos))
print('center : {}'.format(center))
for i in range(int(N[0])):
    k = i
    for j in range(int(N[1])):
        # print('j : {}'.format(j))
        if i == center:
            if j == welcome_pos:
                print(msg, end = '')
            elif j > welcome_pos and j <= welcome_pos + len(msg):
                continue
        elif i < center:
            if j > 3 * abs(i - center) and j <= 3 * (i * 2 + 1) + 3 * abs(i - center):
                continue
            elif j == 3 * abs(i - center):
                for k in range(k * 2 + 1):
                    print(door, end='')
        elif i > center:
            if j > 3 * abs(i - center) and j <= 3 * ((row - 1 - i) * 2 + 1) + 3 * abs(i - center):
                continue
            elif j == 3 * abs(i - center):
                for k in range((row - 1 - k) * 2 + 1):
                    print(door, end='')
        print('-', end = '')
    else:
        print('')