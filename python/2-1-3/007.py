from collections import deque
 
r, c = map(int, input().split())
sx, sy = map(int, input().split())
gx, gy = map(int, input().split())
Map = [list(input()) for _ in range(r)]
 
Map[sx-1][sy-1] = 0
moved = [[1, 0], [-1, 0], [0, 1], [0, -1]]
 
stack = deque([(sx-1, sy-1)])
while stack:
    x,y = stack.popleft()
    
    for i,j in moved:
        if Map[x+i][y+j] != '.':
            continue
        stack.append((x+i,y+j))
        Map[x+i][y+j] = Map[x][y] + 1
 
print(Map[gx-1][gy-1])