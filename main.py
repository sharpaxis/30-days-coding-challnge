# input string
string = input("enter string: ").strip().lower()
# counting occurrence of character
count = 0
# checking if char is found
char_found = False
for i in string:
    j = 0
    while j < len(string):
        if string[j] == i:
            count += 1
        j += 1
    if count == 1:
        print(f"char: {i}")
        char_found = True
        break
    count = 0



