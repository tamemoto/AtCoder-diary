n, res = map(int, input().split())
for x in range(n + 1):
    for y in range(n - x + 1):
        z = n - x - y
        if res == 10000 * x + 5000 * y + 1000 * z:
            print(x, y, z)
            exit()
print("-1 -1 -1")
