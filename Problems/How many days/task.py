seconds = [86400, 1028397, 8372891, 219983, 865779330, 3276993204380912]
days = [int(day / 60 / 60 // 24) for day in seconds]
print(days)
