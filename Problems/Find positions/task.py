numbers = input().split()
target_num = input()
positions = [str(i) for i in range(len(numbers)) if numbers[i] == target_num]
print(' '.join(positions) if positions else "not found")
