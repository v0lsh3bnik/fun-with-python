file = open('gen.txt', 'a')

schema = '0123456789'
characters = list(schema)
arr = []
min_ = 2
high_ = 4

combinations = ['0' for i in range(high_)]


def update_pos(_param, _combination, _pos, _file):
    _combination[pos] = _param
    _file.write(''.join(_combination) + '\n')


for i in range(len(combinations), 0, -1):
    pos = i - 1
    if pos == 3:
        for f in list(schema):
            update_pos(f, combinations, pos + 3, file)
    elif pos == 2:
        for f in list(schema):
            combinations[pos] = f
            for y in list(schema):
                update_pos(y, combinations, pos + 1, file)
    elif pos == 1:
        for f in list(schema):
            combinations[pos] = f
            for y in list(schema):
                combinations[pos + 1] = y
                for z in list(schema):
                    update_pos(z, combinations, pos + 2, file)
    elif pos == 0:
        for f in list(schema):
            combinations[pos] = f
            for y in list(schema):
                combinations[pos + 1] = y
                for z in list(schema):
                    update_pos(z, combinations, pos + 2, file)
                    for v in list(schema):
                        update_pos(v, combinations, pos + 3, file)

# # Driver Function
# if __name__ == "__main__":
#     pass
