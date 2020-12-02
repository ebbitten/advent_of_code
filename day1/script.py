with open('data') as f:
    data = [int(line) for line in f.readlines()]
print(data)
for x in data:
    for y in data:
        for z in data:
            if sum([x,y,z]) == 2020:
                print(x, y, z, x*y*z)