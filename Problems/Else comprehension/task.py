# the following line reads the list from the input, do not modify it, please
old_list = [int(num) for num in input().split()]

binary_list = [1 if number > 0 else 0 for number in old_list]
print(binary_list)
