

lines = ["1007125",
         "13, x, x, 41, x, x, x, x, x, x, x, x, x, 569, x, 29, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, 19, x, x, x, 23, x, x, x, x, x, x, x, 937, x, x, x, x, x, 37, x, x, x, x, x, x, x, x, x, x, 17"]

buses = [int(x.replace("x", "1")) for x in lines[1].split(",")]
m = max(buses)
m_ind = buses.index(m)

indexed = []
for b in enumerate(buses):
    if b[1] != 1:
        indexed.append(((b[0]-m_ind), b[1]))

indexed.sort(reverse=True, key=lambda x: x[1])

#this is the Chinese Remainder Therom 
curr = 0
inc = m
fixed = 1
indexed = indexed[1:]
while True:
    curr += inc
    for i, b in enumerate(indexed):
        if (curr + b[0]) % b[1] != 0:
            break
        elif i == len(indexed)-1:
            print(curr-m_ind)
            quit()
        else:
            inc = inc * b[1]
            indexed = indexed[1:]
            print("{}: {} {}".format(curr, inc, indexed))


