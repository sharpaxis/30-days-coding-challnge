# input of strings and unpacking
string_1 = input("enter string: ").lower().strip()
l_string_1 = [*string_1]
string_2 = input("enter string: ").lower().strip()
l_string_2 = [*string_2]
# checking if both are strings
if string_1.isalpha() and string_2.isalpha():
    # lex sort
    i = 0
    while i < len(l_string_1)-1:
        if l_string_1[i] > l_string_1[i+1]:
            l_string_1[i],l_string_1[i+1] = l_string_1[i+1],l_string_1[i]
            # resetting value of i to make sure loop start from beginning
            i = -1
        i += 1
    j = 0
    while j < len(l_string_2)-1:
        if l_string_2[j] > l_string_2[j+1]:
            l_string_2[j], l_string_2[j+1] = l_string_2[j+1], l_string_2[j]
            # resetting value of i to make sure loop start from beginning
            j = -1
        j += 1
    # both strings are sorted
    # joining strings
    f_str_1 = "".join(l_string_1)
    f_str_2 = "".join(l_string_2)
    # checking if sorted string are same
    if f_str_1 == f_str_2:
        print("True")
    else:
        print("False")
# if input is not a string
else:
    raise ValueError("Enter a string")

