word_list = input().split()
s_words = [word for word in word_list if word.endswith('s')]
print('_'.join(s_words))
