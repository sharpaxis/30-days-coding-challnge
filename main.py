#creating array from input
#number of elements in list
n = int(input("number of elements in the list: "))
num_array = []
for i in range(n):
    num = int(input("enter number: "))
    num_array.append(num)
#kth element input
k_max = int(input("kth element: "))
#finding the kth max element
for _ in range(k_max-1):
    max_ele = max(num_array)
    num_array.remove(max_ele)
print("The kth max num is: ",max(num_array))


