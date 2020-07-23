import itertools
import math



def main(count):
    now_count = 0
    data = []
    while now_count < count:
        place_info = input().split()
        place = (int(place_info[0]), int(place_info[1]))
        data.append(place)
        now_count +=1

    result = None
    for v in list(itertools.combinations(data, 2)):
        dis = math.sqrt(abs(v[0][0] - v[1][0])**2 + abs(v[0][1] - v[1][1])**2)
        if result == None:
            result = dis
        elif result < dis:
            result = dis
    return result


count = int(input())
print(main(count))