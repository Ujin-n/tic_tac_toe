num_list = [int(i) for i in input()]
avg_list = [(num_list[i] + num_list[i + 1]) / 2 for i in range(len(num_list) - 1)]
print(avg_list)
