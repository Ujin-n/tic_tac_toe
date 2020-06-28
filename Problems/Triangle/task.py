number = int(input())

for i in range(number):
    print(('#' + '##' * i).center(number * 2))
