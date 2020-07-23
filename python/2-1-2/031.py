
field = [list(input()), for _ in range(10)]
import sys
sys.setrecursionlimit(10**7)

def search(x, y):
    if not(0<=x<=9) or not(0<=y<=9):
        return
