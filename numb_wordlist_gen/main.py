file = open('gen.txt', 'a')

schema = '0123456789'
characters = list(schema)
arr = []
min_ = 2
high_ = 4

combinations = ['0' for i in range(high_)]

for i in range(len(combinations), 0, -1):
    pos = i - 1
    if pos == 3:
        for f in list(schema):
            combinations[pos] = f
            file.write(''.join(combinations) + '\n')
    elif pos == 2:
        for f in list(schema):
            combinations[pos] = f
            for y in list(schema):
                combinations[pos + 1] = y
                file.write(''.join(combinations) + '\n')
    elif pos == 1:
        for f in list(schema):
            combinations[pos] = f
            for y in list(schema):
                combinations[pos + 1] = y
                for z in list(schema):
                    combinations[pos + 2] = z
                    file.write(''.join(combinations) + '\n')
    elif pos == 0:
        for f in list(schema):
            combinations[pos] = f
            for y in list(schema):
                combinations[pos + 1] = y
                for z in list(schema):
                    combinations[pos + 2] = z
                    file.write(''.join(combinations) + '\n')
                    for v in list(schema):
                        combinations[pos + 3] = v
                        file.write(''.join(combinations) + '\n')

    file.write('*' * 10 + '\n')

print(combinations)
print(arr)

# # Driver Function
# if __name__ == "__main__":
#     pass
