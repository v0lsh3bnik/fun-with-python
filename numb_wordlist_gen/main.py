# v0l5h3bn1k ~ https://github.com/v0lsh3bnik/fun-with-python

def update_pos(_param, _combination, _pos, _file):
    _combination[_pos] = _param
    _file.write(''.join(_combination) + '\n')


# code in gen_code() generates duplicates, so had to clean them before I look at the logic
# using sets to get unique values
# final generated file 10k values (my only way to verify it s ok, since 4 code
# combinations of 0 - 9 have 10000 possible outcomes)
def remove_duplicates():
    raw_file = open('raw.txt', 'r')
    gen_file = open('gen.txt', 'a')
    data = []
    for line in raw_file:
        data.append(line.strip())
    for d in set(data):
        gen_file.write(str(d) + '\n')
    raw_file.close()
    gen_file.close()

# to be honest, code feels a bit dodgy. Any ideas ?
def gen_codes():
    file = open('raw.txt', 'a')

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
                update_pos(f, combinations, pos, file)
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

    file.close()


if __name__ == "__main__":
    gen_codes()
    remove_duplicates()
