in_list = [int(number) for number in input()]
print([sum(in_list[:i + 1]) for i in range(len(in_list))])
