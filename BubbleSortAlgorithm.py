input = [16, 45, 16, 19, 24, 50]
length=len(input)
for y in range(len(input)-1):
    for x in range(length):
        if x+1 < length and input[x] > input[x+1]:
            lowerValue = input[x+1]
            input[x+1] = input[x]
            input[x] = lowerValue
    length = length - 1

print input
