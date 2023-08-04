# creating array from input
# number of elements in list
n = int(input("number of elements in the list: "))
num_array = []
for i in range(n):
    num = int(input("enter number: "))
    num_array.append(num)
# traversing array using for loop

for i in range(len(num_array)):
    for j in range(i):
        while i < len(num_array)-1 :
            if num_array[i] > num_array[i+1]:
                num_array[i], num_array[i+1] = num_array[i+1],num_array[i]
            i += 1
        while num_array[j] > num_array[j+1]:
            num_array[j],num_array[j+1] = num_array[j+1],num_array[j]
            j += 1

print(num_array)
