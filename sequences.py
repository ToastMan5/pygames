#length = int(input("Enter number of numbers in sequence: "))
length = 5
#sequence = []
#sequence = [2, 5, 10, 17, 26]
sequence = [4,8,12,16,20]
fdiff = []
sdiff = []
#for i in range(1,length+1): sequence.append(int(input(f"Enter number {i}: ")))
print(f"Sequence: {sequence}")
for i in range(length):
    if i>0:
        fdiff.append(sequence[i]-sequence[i-1])
print(f"First differences: {fdiff}")
for i in range(length-1):
    if i>0:
        sdiff.append(fdiff[i]-fdiff[i-1])
print(f"Second differences: {sdiff}")
if sum(sdiff) == 0:
    print("Sequence is linear")
    if sequence[0]-fdiff[0] == 0 and fdiff[0] == 1:
        print(f"n")
    elif sequence[0]-fdiff[0] == 0: print(f"{fdiff[0]}n")
    else: print(f"{fdiff[0]}n {sequence[0]-fdiff[0]}")
else: print("Sequence is quadratic or more complex")
