# creating array from input
# number of elements in list
n = int(input("number of elements in the list: "))
num_array = []
for i in range(n):
    num = int(input("enter number: "))
    num_array.append(num)

# sorting the array
num_array.sort()
print(num_array)
# element to find
x = int(input("enter element : "))
# count variable
count=0
for j in num_array:
    if j == x:
        count += 1
    # breaking the loop
    if j > x:
        break
print(f'{x} occured {count} times in the array')




