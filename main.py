# creating array from input
# number of elements in list
n = int(input("number of elements in the list: "))
num_array = []
for i in range(n):
    num = int(input("enter number: "))
    num_array.append(num)
sum_arr = int(input("enter the sum: "))
# accessing sub array
sub_arr = []
# boolean if sub array is found
arr_found = False
for i in range(len(num_array)):
    temp_sum = 0
    # to print only one sub array
    if arr_found is True:
        break
    while i < len(num_array) and temp_sum <= sum_arr:
        temp_sum = num_array[i]+temp_sum
        sub_arr.append(num_array[i])
        i = i + 1
        if sum_arr == temp_sum:
            print(sub_arr)
            # breaking loop once array is found
            arr_found = True
            break
    else:
        sub_arr.clear()
# if sub array isn't found
if arr_found is False:
    print("Sub array doesnt exist")
