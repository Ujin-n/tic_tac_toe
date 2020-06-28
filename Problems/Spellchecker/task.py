dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
incorrect_word = []

for word in input().split():
    if word not in dictionary:
        print(word)
        incorrect_word.append(word)

if not incorrect_word:
    print("OK")
