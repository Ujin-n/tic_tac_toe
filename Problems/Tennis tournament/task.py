n = int(input())
res_list = []

for _ in range(n):
    res_list.append(input().split())

win_list = [name for name, res in res_list if res == 'win']

print(win_list)
print(len(win_list))
