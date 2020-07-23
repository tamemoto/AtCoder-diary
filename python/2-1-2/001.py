
max_h, max_w = map(int, input().split())
field = [list(input()) for _ in range(max_h)]
import sys
sys.setrecursionlimit(10**7)

def search(x, y):
    if not(0<=x<=max_h-1) or not(0<=y<=max_w-1) or field[x][y]=="#":
        return  
    if field[x][y] == "g":
        print("Yes")
        exit()
    field[x][y]="#"
    search(x+1, y)
    search(x-1, y)
    search(x, y+1)
    search(x, y-1)



for i in range(max_h):
    for j in range(max_w):
        if field[i][j]=="s":
            sx,sy=i,j

search(sx,sy)
print("No")
