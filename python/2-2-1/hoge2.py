input_data = input()
a = 0
b = 0
for i in range(len(input_data) - 2):
    if input_data[i:i+3] == "JOI":
        a += 1
    if input_data[i:i+3] == "IOI":
        b += 1
print("{0}\n{1}".format(a, b))