words_list = input().split()
print(''.join([words_list[0]] + [word.capitalize() for word in words_list[1:]]))
