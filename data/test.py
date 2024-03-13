import random

C_p = [0 for i in range(1000)]
# print(list)
n = len(C_p)
for i in range(0, n):
    C_p[i] = random.randint(60, 100)

# C_p是60-100的随机数
is_parked = [0 for i in range(n)]

for i in range(n - 2):  # n is the element number of a group
    avg = (C_p[i] + C_p[i+1] + C_p[i+2]) / 3
    if avg >= 80:
        # default value of is_parked is 0
        is_parked[i] = is_parked[i+1] = is_parked[i+2] = 1


# how to check if it's correct?
is_parked_check = [0 for i in range(n)]
for i in range(n):
    thisSUM = C_p[i]
    for j in range(i+1, n):
        thisSUM += C_p[j]
        avg = thisSUM / (j - i + 1)
        if avg >= 80 and j - i + 1 >= 3:
            for k in range(i, j+1):
                is_parked_check[k] = 1

ans = (is_parked == is_parked_check)
c = [is_parked_check[i] - is_parked[i] for i in range(n)]

# print(is_parked)
# print(is_parked_check)
# print(c)
# print(C_p)
# print(C_p)
# print(c)
