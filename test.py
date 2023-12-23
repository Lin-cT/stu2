val = 0
sum = 0
print("Val= " + str(val))
print("Sum= " + str(sum))

for i in range(10):
    val = val + 2
    print("Val= " + str(val))
    sum = sum + val
    print("Sum= " + str(sum))

print("Total Sum= " + str(sum))