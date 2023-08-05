# creating array from input
# number of elements in list
n = int(input("number of elements in the list: "))
num_array = []
for i in range(n):
    num = int(input("enter number: "))
    num_array.append(num)
sum_p = int(input("enter sum: "))
count = 0
for j in range(len(num_array)):
    for k in range(j+1,len(num_array)):
        if num_array[j] + num_array[k] == sum_p:
            if j != k:
                count += 1
print(count)


