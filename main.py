def knapsack(C, weight, cost, n):
    K = [[0 for x in range(C + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for j in range(C + 1):
            if i == 0 or j == 0:
                K[i][j] = 0
            elif weight[i - 1] <= j:
                K[i][j] = max(cost[i - 1][0] + K[i - 1][j - weight[i - 1]], K[i - 1][j])
            else:
                K[i][j] = K[i - 1][j]
    return K

backpack = {}

stuffdict = {'в': (3, 25),
             'п': (2, 15),
             'б': (2, 15),
             'а': (2, 20),
             'н': (1, 15),
             'т': (3, 20),
             'о': (1, 25),
             'ф': (1, 15),
             'д': (1, 10),
             'к': (2, 20),
             'р': (2, 20)
             }
values = []
weights = []
capacity = 8
init_points = 10

for key in stuffdict:
    weights.append([stuffdict[key][1], key])
    values.append(stuffdict[key][0])

count = len(values)

K = knapsack(capacity, values, weights, count)

j, i, total = capacity, count, 0
result = K[count][capacity]
while i > 0 and result > 0:
    if result != K[i - 1][j]:
        backpack[weights[i - 1][1]] = [weights[i - 1][0], values[i - 1]]
        stuffdict.pop(weights[i-1][1])
        total += values[i - 1]
        result -= weights[i - 1][0]
        j -= values[i - 1]
    i -= 1

L = 0
for key in backpack:
    for k in range(backpack[key][1]):
        if L == 3:
            print("\b\b")
            L = 0
        print(key, end=', ')
        L += 1
print("и")

start = 10
sum = 0
print(stuffdict)
for key in stuffdict:
    sum += stuffdict[key][1]
print("Итоговые очки выживания: ", K[count][capacity] + 5 - sum + start)

